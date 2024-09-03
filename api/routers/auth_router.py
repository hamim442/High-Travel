from fastapi import (
    Depends,
    Request,
    Response,
    HTTPException,
    status,
    APIRouter,
)
from queries.user_queries import (
    UserQueries,
)
from utils.exceptions import UserDatabaseException
from models.users import (
    UserResponse,
    SigninRequest,
    SignupRequest,
    UpdateUserRequest,
)

from utils.authentication import (
    try_get_jwt_user_data,
    hash_password,
    generate_jwt,
    verify_password,
)

from models.jwt import JWTUserData

from typing import Optional

# Note we are using a prefix here,
# This saves us typing in all the routes below
router = APIRouter(tags=["Authentication"], prefix="/api/auth")


@router.post("/signup")
async def signup(
    new_user: SignupRequest,
    request: Request,
    response: Response,
    queries: UserQueries = Depends(),
) -> UserResponse:
    hashed_password = hash_password(new_user.password)

    # Todo upload the file

    try:
        user = queries.create_user(
            new_user.username,
            hashed_password,
            new_user.email,
            new_user.first_name,
            new_user.last_name,
            new_user.profile_image,
        )
    except UserDatabaseException as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    token = generate_jwt(user)
    user_out = UserResponse(**user.model_dump())
    secure = True if request.headers.get("origin") == "localhost" else False

    response.set_cookie(
        key="fast_api_token",
        value=token,
        httponly=True,
        samesite="lax",
        secure=secure,
    )
    return user_out


@router.post("/signin")
async def signin(
    user_request: SigninRequest,
    request: Request,
    response: Response,
    queries: UserQueries = Depends(),
) -> UserResponse:

    user = queries.get_by_username(user_request.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    if not verify_password(user_request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    token = generate_jwt(user)

    secure = True if request.headers.get("origin") == "localhost" else False

    response.set_cookie(
        key="fast_api_token",
        value=token,
        httponly=True,
        samesite="lax",
        secure=secure,
    )

    # Convert the UserWithPW to a UserOut
    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        profile_image=user.profile_image,
    )


@router.get("/authenticate")
async def authenticate(
    jwt_user: JWTUserData | None = Depends(
        try_get_jwt_user_data,
    ),
    queries: UserQueries = Depends(),
) -> UserResponse:
    """
    The `try_get_jwt_user_data` function tries to get the user and validate
    the JWT

    If the user isn't logged in this returns a 404

    This can be used in your frontend to determine if a user
    is logged in or not
    """
    if not jwt_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not logged in"
        )
    user = queries.get_by_id(jwt_user.id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not logged in"
        )

    # Convert the UserWithPW to a UserOut
    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        profile_image=user.profile_image,
    )


@router.delete("/signout")
async def signout(
    request: Request,
    response: Response,
):
    secure = True if request.headers.get("origin") == "localhost" else False

    response.delete_cookie(
        key="fast_api_token", httponly=True, samesite="lax", secure=secure
    )

    return


@router.get("/check-username/{username}")
async def check_username(username: str, queries: UserQueries = Depends()):

    try:
        user = queries.get_by_username(username)
        return {"exists": user is not None}
    except UserDatabaseException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.put("/edit-user")
def update_user(
    updaterequest: UpdateUserRequest,
    queries: UserQueries = Depends(),
    jwtuser: JWTUserData | None = Depends(try_get_jwt_user_data),
) -> UserResponse:
    if not jwtuser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    update_user = queries.edit_user(
        user_id=jwtuser.id,
        first_name=updaterequest.first_name,
        last_name=updaterequest.last_name,
        profile_image=updaterequest.profile_image,
    )

    return UserResponse(
        id=update_user.id,
        username=update_user.username,
        email=update_user.email,
        first_name=update_user.first_name,
        last_name=update_user.last_name,
        profile_image=update_user.profile_image,
    )
