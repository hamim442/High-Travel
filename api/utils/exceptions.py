"""
Custom Exceptions for the App
"""


class UserDatabaseException(Exception):
    pass


class DatabaseURLException(Exception):
    pass


class AirlineCreationError(Exception):
    pass


class AirlineDatabaseError(Exception):
    pass


class AirlineDoesNotExist(Exception):
    pass


class CityCreationError(Exception):
    pass


class CityDatabaseError(Exception):
    pass


class CityDoesNotExist(Exception):
    pass


class TripCreationError(Exception):
    pass


class TripDatabaseError(Exception):
    pass


class TripDoesNotExist(Exception):
    pass


class StayCreationError(Exception):
    pass


class StayDatabaseError(Exception):
    pass


class StayDoesNotExist(Exception):
    pass
