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
