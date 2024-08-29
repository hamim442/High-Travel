"""
Database Queries for Users
"""

import os
import psycopg
from psycopg_pool import ConnectionPool
from psycopg.rows import class_row
from typing import Optional
from models.users import UserWithPw
from utils.exceptions import UserDatabaseException
from pydantic import EmailStr

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

pool = ConnectionPool(DATABASE_URL)


class UserQueries:
    """
    Class containing queries for the Users table

    Can be dependency injected into a route like so

    def my_route(userQueries: UserQueries = Depends()):
        # Here you can call any of the functions to query the DB
    """

    def get_by_username(self, username: str) -> Optional[UserWithPw]:
        """
        Gets a user from the database by username

        Returns None if the user isn't found
        """
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(UserWithPw)) as cur:
                    cur.execute(
                        """--sql
                            SELECT
                                *
                            FROM users
                            WHERE username = %s
                            """,
                        [username],
                    )
                    user = cur.fetchone()
                    if not user:
                        return None
        except psycopg.Error as e:
            print(e)
            raise UserDatabaseException(f"Error getting user {username}")
        return user

    def get_by_id(self, id: int) -> Optional[UserWithPw]:
        """
        Gets a user from the database by user id

        Returns None if the user isn't found
        """
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(UserWithPw)) as cur:
                    cur.execute(
                        """--sql
                            SELECT
                                *
                            FROM users
                            WHERE id = %s
                            """,
                        [id],
                    )
                    user = cur.fetchone()
                    if not user:
                        return None
        except psycopg.Error as e:
            print(e)
            raise UserDatabaseException(f"Error getting user with id {id}")

        return user

    def create_user(
        self,
        username: str,
        hashed_password: str,
        email: EmailStr,
        first_name: str,
        last_name: str,
        profile_image: Optional[str] = None,
    ) -> UserWithPw:
        """
        Creates a new user in the database

        Raises a UserInsertionException if creating the user fails
        """
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(UserWithPw)) as cur:
                    cur.execute(
                        """--sql
                        INSERT INTO users (
                            username,
                            password,
                            email,
                            profile_image,
                            first_name,
                            last_name
                        ) VALUES (
                            %s, %s, %s, %s, %s, %s
                        )
                        RETURNING *;
                        """,
                        [
                            username,
                            hashed_password,
                            email,
                            profile_image,
                            first_name,
                            last_name,
                        ],
                    )
                    user = cur.fetchone()
                    if not user:
                        raise UserDatabaseException(
                            f"Could not create user with username {username}"
                        )
        except psycopg.Error:
            raise UserDatabaseException(
                f"Could not create user with username {username}"
            )
        return user

    def edit_user(
        self,
        user_id: int,
        hashed_password: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        profile_image: Optional[str] = None,
    ) -> UserWithPw:
        """
        Updates a user in the database

        Raises an Exception if updating an user fails
        """
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(UserWithPw)) as cur:
                    update_users = []
                    update_values = []
                    if hashed_password:
                        update_users.append("password = %s")
                        update_values.append(hashed_password)
                    if first_name:
                        update_users.append("first_name = %s")
                        update_values.append(first_name)
                    if last_name:
                        update_users.append("last_name = %s")
                        update_values.append(last_name)
                    if profile_image:
                        update_users.append("profile_image = %s")
                        update_values.append(profile_image)
                    update_values.append(user_id)
                    cur.execute(
                        """--sql
                        UPDATE Users
                        SET{', '.join(update_users)}
                        WHERE id = %s
                        RETURNING *;
                        """,
                        update_values,
                    )

                    user = cur.fetchone()
                    if not user:
                        raise UserDatabaseException(
                            f"{user_id} cannot be updated"
                        )
        except psycopg.Error:
            raise UserDatabaseException(f"Could not update user {user_id}")
        return user
