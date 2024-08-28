"""
Pydantic Models for Users.
"""

from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional


class SigninRequest(BaseModel):
    username: str
    password: str


class SignupRequest(BaseModel):
    """
    Represents the parameters needed to create a new user
    """

    username: str
    password: str
    email: EmailStr
    profile_image: Optional[str] = None
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    """
    Represents a user, with the password not included
    """

    id: int
    username: str
    email: EmailStr
    profile_image: HttpUrl
    first_name: str
    last_name: str


class UserWithPw(BaseModel):
    """
    Represents a user with password included
    """

    id: int
    username: str
    password: str
    email: EmailStr
    profile_image: HttpUrl
    first_name: str
    last_name: str
