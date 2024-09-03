import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import useAuthService from '../hooks/useAuthService';
import { useNavigate, useLocation } from 'react-router-dom';
import TransportationDetails from './TransportationDetails';
import AccommodationDetails from './AccommodationDetails';

export default function MainTravelPlan() {
    const { tripId } = useParams();
    const { user } = useAuthService();
    const [trip, setTrip] = useState(null);
    const [city, setCity] = useState(null);
    const [flights, setFlights] = useState([]);
    const [trains, setTrains] = useState([]);
    const [cars, setCars] = useState([]);
    const [accommodations, setAccommodations] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const navigate = useNavigate();
    const location = useLocation();

    const totalPrice = trains.reduce((total, train) => total + train.price, 0) +
                   cars.reduce((total, car) => total + car.price, 0) +
                   flights.reduce((total, flight) => total + flight.price, 0) +
                   accommodations.reduce((total, accommodation) => total + accommodation.total_price, 0);

    useEffect(() => {
        async function checkAuth() {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/auth/authenticate`,
                { credentials: 'include' }
            );
            if (!response.ok) {
                navigate('/signin', { state: { from: location.pathname } });
            }
        }
        checkAuth();
    }, [navigate, location]);

    useEffect(() => {
        async function fetchData() {
            setLoading(true);
            setError(null);
            try {
                const tripResponse = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/trips/${tripId}`,
                    { credentials: 'include' }
                );
                if (!tripResponse.ok) {
                    throw new Error('Failed to fetch trip data');
                }
                const tripData = await tripResponse.json();
                setTrip(tripData);

                const cityResponse = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/cities/${tripData.city_id}`,
                    { credentials: 'include' }
                );
                if (!cityResponse.ok) {
                    throw new Error('Failed to fetch city data');
                }
                const cityData = await cityResponse.json();
                setCity(cityData);

                const trainsResponse = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/trains`,
                    { credentials: 'include' }
                );
                if (!trainsResponse.ok) {
                    throw new Error('Failed to fetch train data');
                }
                const trainsData = await trainsResponse.json();
                const filteredTrains = trainsData.filter(train => train.trip_id === parseInt(tripId));
                setTrains(filteredTrains);

                const carsResponse = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/cars`,
                    { credentials: 'include' }
                );
                if (!carsResponse.ok) {
                    throw new Error('Failed to fetch car rental data');
                }
                const carsData = await carsResponse.json();
                const filteredCars = carsData.filter(car => car.trip_id === parseInt(tripId));
                setCars(filteredCars);

                const flightsResponse = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/flights`,
                    { credentials: 'include' }
                );
                if (!flightsResponse.ok) {
                    throw new Error('Failed to fetch flight data');
                }
                const flightsData = await flightsResponse.json();
                const filteredFlights = flightsData.filter(flight => flight.trip_id === parseInt(tripId));
                setFlights(filteredFlights);

                const accommodationsResponse = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/accommodations`,
                    { credentials: 'include' }
                );
                if (!accommodationsResponse.ok) {
                    throw new Error('Failed to fetch accommodations');
                }
                const accommodationsData = await accommodationsResponse.json();
                const filteredAccommodations = accommodationsData.filter(accommodation => accommodation.trip_id === parseInt(tripId));
                setAccommodations(filteredAccommodations);

            } catch (error) {
                console.error('Error fetching data: ', error);
                setError('Failed to load data. Please try again later.');
            } finally {
                setLoading(false);
            }
        }

        fetchData();
    }, [tripId]);

    const deleteFlight = async (id) => {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/flights/${id}`,
                { method: 'DELETE', credentials: 'include' }
            );

            if (!response.ok) {
                throw new Error('Failed to delete flight');
            }

            setFlights(flights.filter(flight => flight.id !== id));
        } catch (error) {
            console.error('Error deleting flight:', error);
            setError('Failed to delete flight. Please try again.');
        }
    };

    const handleDeleteFlight = (id) => {
        if (window.confirm('Are you sure you want to delete this flight?')) {
            deleteFlight(id);
        }
    };

    const deleteTrain = async (id) => {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/trains/${id}`,
                { method: 'DELETE', credentials: 'include' }
            );

            if (!response.ok) {
                throw new Error('Failed to delete trains');
            }

            setTrains(trains.filter(train => train.id !== id));
        } catch (error) {
            console.error('Error deleting train:', error);
            setError('Failed to delete train. Please try again.');
        }
    };

    const handleDeleteTrain = (id) => {
        if (window.confirm('Are you sure you want to delete this train?')) {
            deleteTrain(id);
        }
    };

    const deleteCar = async (id) => {
    try {
        const response = await fetch(
            `${import.meta.env.VITE_API_HOST}/api/cars/${id}`,
            { method: 'DELETE', credentials: 'include' }
        );

        if (!response.ok) {
            throw new Error('Failed to delete car');
        }

        setCars(cars.filter(car => car.id !== id));
    } catch (error) {
        console.error('Error deleting car:', error);
        setError('Failed to delete car. Please try again.');
    }
};

const handleDeleteCar = (id) => {
    if (window.confirm('Are you sure you want to delete this car?')) {
        deleteCar(id);
    }
};

const deleteTrip = async () => {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/trips/${tripId}`,
                { method: 'DELETE', credentials: 'include' }
            );

            if (!response.ok) {
                throw new Error('Failed to delete trip');
            }

            navigate('/profile');
        } catch (error) {
            console.error('Error deleting trip:', error);
            setError('Failed to delete trip. Please try again.');
        }
    };

    const handleDeleteTrip = () => {
        if (window.confirm('Are you sure you want to delete this trip?')) {
            deleteTrip();
        }
    };

    const deleteAccommodation = async (id) => {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/accommodations/${id}`,
                { method: 'DELETE', credentials: 'include' }
            );

            if (!response.ok) {
                throw new Error('Failed to delete accommodation');
            }

            setAccommodations(accommodations.filter(accommodation => accommodation.id !== id));
        } catch (error) {
            console.error('Error deleting accommodation:', error);
            setError('Failed to delete accommodation. Please try again.');
        }
    };

    const handleDeleteAccommodation = (id) => {
        if (window.confirm('Are you sure you want to delete this accommodation?')) {
            deleteAccommodation(id);
        }
    };

    if (loading) {
        return <p>Loading...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    if (!trip) {
        return <p>No trip data available.</p>;
    }

    return (
        <div className="container">

            <div className="mt-4">
                <h2>{user.username}'s trip to {city.name}</h2>
                <div className="row align-items-center mt-3">
                    <div className="col-md-4">
                        <div className="bg-light border" style={{ height: '210px' }}>
                            {city?.picture_url && (
                                <img
                                    src={city.picture_url}
                                    alt={`View of ${city.name}`}
                                    style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                                />
                            )}
                        </div>
                    </div>
                    <div className="col-md-6">
                        <div className="bg-light p-3">
                            <p>{city.name}, {city.administrative_division}, {city.country}</p>
                            <p>
                                Start Date: {new Date(trip.start_date).toLocaleDateString()} <br />
                                End Date: {new Date(trip.end_date).toLocaleDateString()}
                            </p>
                            <p>
                                Total Price: ${totalPrice}
                            </p>
                            <button className="btn btn-primary" onClick={handleDeleteTrip}>Delete Trip</button>
                        </div>
                    </div>
                    <div className="col-md-2 text-right">
                        <div>
                            {/* Placeholder for social icons, stretch goal */}
                        </div>
                    </div>
                </div>
            </div>

            <div className="row mt-4">
                <div className="col-md-4">
                    <TransportationDetails tripId={tripId} trains={trains} cars={cars} flights={flights} handleDeleteFlight={handleDeleteFlight} handleDeleteTrain={handleDeleteTrain} handleDeleteCar={handleDeleteCar} />
                </div>

                <div className="col-md-4">
                    <AccommodationDetails tripId={tripId} accommodations={accommodations} handleDeleteAccommodation={handleDeleteAccommodation} />
                </div>

                {/* strech goal */}

                <div className="col-md-4">
                    <div className="card">
                        <div className="card-body">
                            <h5 className="card-title">Food/Places/Others</h5>
                            <p className="card-text">Details about food/places/others</p>
                        </div>
                        <div className="card-footer text-right">
                            <p>Total Price: $0</p>
                            <button className="btn btn-success">+</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
