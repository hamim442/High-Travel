import os
import psycopg
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool
from models.accommodations import (
    Accommodation,
    AccommodationRequest,
    AccommodationUpdate,
)
from utils.exceptions import (
    AccommodationDatabaseError,
    AccommodationDoesNotExist,
    AccommodationCreationError,
    DatabaseURLException,
)


database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException(
        "You forgot to define DATABASE_URL in your environment."
    )

pool = ConnectionPool(database_url)


class AccommodationQueries:

    def get_all_accommodations(self, user_id: int) -> list[Accommodation]:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Accommodation)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT accommodations.*
                            FROM accommodations
                            JOIN trips ON accommodations.trip_id = trips.id
                            WHERE trips.user_id = %s;
                        """,
                        (user_id,),
                    )
                    accommodations = result.fetchall()
                    return accommodations
        except psycopg.Error as e:
            print(f"Error retrieving accommodations: {e}")
            raise AccommodationDatabaseError(
                "Error retrieving accommodations."
            )

    def get_accommodation(self, id: int, user_id: int) -> Accommodation:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Accommodation)) as cur:
                    result = cur.execute(
                        """--sql
                            SELECT accommodations.*
                            FROM accommodations
                            JOIN trips ON accommodations.trip_id = trips.id
                            WHERE accommodations.id = %s AND trips.user_id = %s;
                        """,
                        (id, user_id),
                    )
                    accommodation = result.fetchone()
                    if accommodation is None:
                        raise AccommodationDoesNotExist(
                            f"No accommodation with id {id}."
                        )
                    return accommodation
        except psycopg.Error as e:
            print(f"Error retrieving accommodation with id {id}: {e}.")
            raise AccommodationDatabaseError(
                f"Error retrieving accommodation with id {id}."
            )

    def create_accommodation(
        self, accommodation: AccommodationRequest
    ) -> Accommodation:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Accommodation)) as cur:
                    result = cur.execute(
                        """--sql
                            INSERT INTO accommodations (
                                stays_id, address, city, state_province, zip_code, country,
                                phone, email, check_in_date, check_out_date,
                                number_of_guests, total_price, notes, trip_id
                            )
                            VALUES (
                                %(stays_id)s, %(address)s, %(city)s, %(state_province)s, %(zip_code)s,
                                %(country)s, %(phone)s, %(email)s, %(check_in_date)s, %(check_out_date)s,
                                %(number_of_guests)s, %(total_price)s, %(notes)s, %(trip_id)s
                            )
                            RETURNING *;
                        """,
                        accommodation.model_dump(),
                    )
                    new_accommodation = result.fetchone()
                    if new_accommodation is None:
                        raise AccommodationCreationError(
                            "Error creating accommodation."
                        )
                    return new_accommodation
        except psycopg.Error as e:
            print(f"Error creating accommodation: {e}.")
            raise AccommodationDatabaseError("Error creating accommodation.")

    def delete_accommodation(self, id: int, user_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """--sql
                            DELETE FROM accommodations
                            USING trips
                            WHERE accommodations.id = %s AND trips.user_id = %s
                            AND accommodations.trip_id = trips.id;
                        """,
                        (id, user_id),
                    )
                    return cur.rowcount > 0
        except psycopg.Error as e:
            print(f"Error deleting accommodation with id {id}: {e}.")
            raise AccommodationDatabaseError(
                f"Error deleting accommodation with id {id}."
            )

    def update_accommodation(
        self,
        id: int,
        user_id: int,
        accommdation: AccommodationUpdate,
    ) -> Accommodation:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(Accommodation)) as cur:
                    update_fields = []
                    update_values = []

                    # Add fields to update if provided
                    if accommdation.stays_id is not None:
                        update_fields.append("stays_id = %s")
                        update_values.append(accommdation.stays_id)
                    if accommdation.address is not None:
                        update_fields.append("address = %s")
                        update_values.append(accommdation.address)
                    if accommdation.city is not None:
                        update_fields.append("city = %s")
                        update_values.append(accommdation.city)
                    if accommdation.zip_code is not None:
                        update_fields.append("zip_code = %s")
                        update_values.append(accommdation.zip_code)
                    if accommdation.country is not None:
                        update_fields.append("country = %s")
                        update_values.append(accommdation.country)
                    if accommdation.phone is not None:
                        update_fields.append("phone = %s")
                        update_values.append(accommdation.phone)
                    if accommdation.email is not None:
                        update_fields.append("email = %s")
                        update_values.append(accommdation.email)
                    if accommdation.check_in_date is not None:
                        update_fields.append("check_in_date = %s")
                        update_values.append(accommdation.check_in_date)
                    if accommdation.check_out_date is not None:
                        update_fields.append("check_out_date = %s")
                        update_values.append(accommdation.check_out_date)
                    if accommdation.number_of_guests is not None:
                        update_fields.append("number_of_guests = %s")
                        update_values.append(accommdation.number_of_guests)
                    if accommdation.total_price is not None:
                        update_fields.append("total_price = %s")
                        update_values.append(accommdation.total_price)
                    if accommdation.notes is not None:
                        update_fields.append("notes = %s")
                        update_values.append(accommdation.notes)

                    update_values.append(id)
                    update_values.append(user_id)

                    sql = f"""
                        UPDATE accommodations
                        SET {','.join(update_fields)}
                        FROM trips
                        WHERE accommodations.id = %s  
                        AND accommodations.trip_id = trips.id  -- Corrected table name and field
                        AND trips.user_id = %s
                        RETURNING accommodations.*;
                    """
                    cur.execute(sql, update_values)

                    updated_accommodation = cur.fetchone()

                    if not updated_accommodation:
                        raise AccommodationDoesNotExist(
                            f"Accommodation with id {id} for user {user_id} cannot be updated."
                        )

                    return updated_accommodation

        except psycopg.Error as e:
            print(f"Error updating accommodation with id {id}: {e}.")
            raise AccommodationDatabaseError(
                f"Could not update accommodation with id {id}."
            )
