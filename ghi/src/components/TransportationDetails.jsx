import { NavLink } from 'react-router-dom';

export default function TransportationDetails({ tripId, trains, cars, flights, handleDeleteFlight, handleDeleteTrain, handleDeleteCar }) {
    const totalPrice = trains.reduce((total, train) => total + train.price, 0) +
                   cars.reduce((total, car) => total + car.price, 0) +
                   flights.reduce((total, flight) => total + flight.price, 0);

    return (
        <div className="card">
            <div className="card-body">
                <h5 className="card-title">Transportation</h5>
                {trains.length > 0 ? (
                    <div>
                        <h6 className="card-subtitle mb-2">Trains</h6>
                        {trains.map((train) => (
                            <div key={train.id} className="card mb-3">
                                <div className="card-body">
                                    <h6 className="card-subtitle mb-2 text-muted">Train Number: {train.train_number}</h6>
                                    <p className="card-text">
                                        Departure: {train.departure_station} at {new Date(train.departure_time).toLocaleString()}
                                    </p>
                                    <p className="card-text">
                                        Arrival: {train.arrival_station} at {new Date(train.arrival_time).toLocaleString()}
                                    </p>
                                    <p className="card-text">Price: ${train.price}</p>
                                    <button
                                        className="btn btn-danger"
                                        onClick={() => handleDeleteTrain(train.id)}
                                    >
                                        Delete
                                    </button>
                                </div>
                            </div>
                        ))}
                    </div>
                ) : (
                    <p className="card-text">No train details available.</p>
                )}
                {cars.length > 0 ? (
                    <div>
                        <h6 className="card-subtitle mb-2">Car Rentals</h6>
                        {cars.map((car) => (
                            <div key={car.id} className="card mb-3">
                                <div className="card-body">
                                    <h6 className="card-subtitle mb-2 text-muted">Car Model: {car.car_model}</h6>
                                    <p className="card-text">
                                        Rental Company: {car.rental_company}
                                    </p>
                                    <p className="card-text">
                                        Pickup: {car.pickup_location} at {new Date(car.pickup_time).toLocaleString()}
                                    </p>
                                    <p className="card-text">
                                        Dropoff: {car.dropoff_location} at {new Date(car.dropoff_time).toLocaleString()}
                                    </p>
                                    <p className="card-text">Price: ${car.price}</p>
                                    <button
                                        className="btn btn-danger"
                                        onClick={() => handleDeleteCar(car.id)}
                                    >
                                        Delete
                                    </button>
                                </div>
                            </div>
                        ))}
                    </div>
                ) : (
                    <p className="card-text">No car rental details available.</p>
                )}
                {flights.length > 0 ? (
                    <div>
                        <h6 className="card-subtitle mb-2">Flights</h6>
                        {flights.map((flight) => (
                            <div key={flight.id} className="card mb-3">
                                <div className="card-body">
                                    <h6 className="card-subtitle mb-2 text-muted">Flight Number: {flight.flight_number}</h6>
                                    <p className="card-text">
                                        Airline: {flight.airline_name}
                                    </p>
                                    <p className="card-text">
                                        Departure: {flight.departure_airport} at {new Date(flight.departure_time).toLocaleString()}
                                    </p>
                                    <p className="card-text">
                                        Arrival: {flight.arrival_airport} at {new Date(flight.arrival_time).toLocaleString()}
                                    </p>
                                    <p className="card-text">Price: ${flight.price}</p>
                                    <button
                                        className="btn btn-danger"
                                        onClick={() => handleDeleteFlight(flight.id)}
                                    >
                                        Delete
                                    </button>
                                </div>
                            </div>
                        ))}
                    </div>
                ) : (
                    <p className="card-text">No flight details available.</p>
                )}
            </div>
            <div className="card-footer text-right">
                 <p>Total Price: ${totalPrice}</p>
                <NavLink to={`/trips/${tripId}/transportation`} className="btn btn-success">
                    +
                </NavLink>
            </div>
        </div>
    );
}
