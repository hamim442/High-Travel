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


class AccommodationCreationError(Exception):
    pass


class AccommodationDatabaseError(Exception):
    pass


class AccommodationDoesNotExist(Exception):
    pass


class UserTripDatabaseError(Exception):
    pass


class UserTripCreationError(Exception):
    pass


class FlightDatabaseError(Exception):
    pass


class FlightDoesNotExist(Exception):
    pass


class FlightCreationError(Exception):
    pass


class TrainDatabaseError(Exception):
    pass


class TrainDoesNotExist(Exception):
    pass


class TrainCreationError(Exception):
    pass


class CarDatabaseError(Exception):
    pass


class CarDoesNotExist(Exception):
    pass


class CarCreationError(Exception):
    pass
