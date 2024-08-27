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
)

from utils.authentication import (
    try_get_jwt_user_data,
    hash_password,
    generate_jwt,
    verify_password,
)

router = APIRouter(tags=["Authentication"], prefix="/api/auth")


@router.post("/signup")
async def signup(
    new_user: SignupRequest,
    request: Request,
    response: Response,
    queries: UserQueries = Depends(),
) -> UserResponse:
    hashed_password = hash_password(new_user.password)

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
    user: UserResponse | None = Depends(try_get_jwt_user_data),
) -> UserResponse:

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not logged in"
        )
    return user


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
