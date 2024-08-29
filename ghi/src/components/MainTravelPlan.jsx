import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';
import useAuthService from '../hooks/useAuthService'
import { useNavigate } from 'react-router-dom';

export default function MainTravelPlan() {
    const { tripId } = useParams();
    const { user } = useAuthService();
    const [trip, setTrip] = useState(null);
    const [city, setCity] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const navigate = useNavigate();
    console.log(user)
    console.log(city)
    console.log(trip)

    useEffect(() => {
        async function checkAuth() {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/auth/authenticate`,
                { credentials: 'include' }
            )
            if (!response.ok) {
                navigate('/signin')
            }
        }
        checkAuth()
    }, [navigate])

    useEffect(() => {
        async function fetchTripData() {
            setLoading(true);
            setError(null);
            try {
                const response = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/trips/${tripId}`,
                    { credentials: 'include' }
                );
                if (!response.ok) {
                    throw new Error('Failed to fetch trip data');
                }
                const data = await response.json();
                console.log('Trip Data:', data);
                setTrip(data);
            } catch (error) {
                console.error('Error fetching trip data: ', error);
                setError('Failed to load trip data. Please try again later.');
            } finally {
                setLoading(false);
            }
        }

        fetchTripData();
    }, [tripId]);

    useEffect(() => {
        async function fetchCityData() {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/cities/${trip.city_id}`,
                { credentials: 'include' }
            );
            const cityData = await response.json();
            setCity(cityData);
        }

        if (trip) {
            fetchCityData();
        }
    }, [trip]);


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
                <h2>Trip Name (Trip ID: {tripId})</h2> {/* Display the tripId */}
                <div className="row align-items-center mt-3">
                    <div className="col-md-4">
                        <div className="bg-light border" style={{ height: '150px' }}>
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
                            <p>
                                Start Date: {new Date(trip.start_date).toLocaleDateString()} <br />
                                End Date: {new Date(trip.end_date).toLocaleDateString()}
                            </p>
                            <button className="btn btn-primary">Edit / Delete</button>
                        </div>
                    </div>
                    <div className="col-md-2 text-right">
                        <div>
                            {/* Placeholder for social icons */}
                        </div>
                    </div>
                </div>
            </div>

            <div className="mt-5">
                <div className="row">
                    <div className="col-md-4">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Transportation</h5>
                                <p className="card-text">Details about transportation</p>
                                <button className="btn btn-secondary">Edit / Delete</button>
                            </div>
                            <div className="card-footer text-right">
                                <NavLink to="/transportation" className="btn btn-success">
                                    +
                                </NavLink>
                            </div>
                        </div>
                    </div>

                    <div className="col-md-4">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Accommodation</h5>
                                <p className="card-text">Details about accommodation</p>
                                <button className="btn btn-secondary">Edit / Delete</button>
                            </div>
                            <div className="card-footer text-right">
                                <button className="btn btn-success">+</button>
                            </div>
                        </div>
                    </div>

                    <div className="col-md-4">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Food/Places/Others</h5>
                                <p className="card-text">Details about food/places/others</p>
                                <button className="btn btn-secondary">Edit / Delete</button>
                            </div>
                            <div className="card-footer text-right">
                                <button className="btn btn-success">+</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
