"""
Pydantic Models for Users.
"""

from pydantic import BaseModel, EmailStr
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


class UserRequest(BaseModel):
    username: str
    email: EmailStr
    profile_image: Optional[str] = None
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    profile_image: Optional[str] = None
    first_name: str
    last_name: str


class UserWithPw(BaseModel):
    id: int
    username: str
    password: str
    email: EmailStr
    profile_image: Optional[str] = None
    first_name: str
    last_name: str
