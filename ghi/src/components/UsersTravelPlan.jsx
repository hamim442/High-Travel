import { useNavigate } from "react-router-dom";
import { useEffect, useState } from 'react';
import useAuthService from '../hooks/useAuthService';
import './styles/RandomDestinations.css';
import SmallFooter from './SmallFooter';

export default function UserTravelPlans() {
    const { user } = useAuthService();
    const navigate = useNavigate();
    const [trips, setTrips] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function checkAuth() {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/auth/authenticate`,
                { credentials: 'include' }
            );
            if (!response.ok) {
                navigate('/signin');
            }
        }
        checkAuth();
    }, [navigate]);

    useEffect(() => {
        async function fetchUserTrips() {
            setLoading(true);
            setError(null);

            try {
                const userTripResponse = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/trips/`,
                    { credentials: 'include' }
                );

                if (!userTripResponse.ok) {
                    throw new Error("Failed to fetch user trips");
                }

                const tripsData = await userTripResponse.json();

                const cityDetailsPromises = tripsData.map(async (trip) => {
                    const cityResponse = await fetch(
                        `${import.meta.env.VITE_API_HOST}/api/cities/${trip.city_id}`
                    );

                    if (!cityResponse.ok) {
                        throw new Error("Failed to fetch city details");
                    }

                    const cityData = await cityResponse.json();
                    return { ...trip, city_name: cityData.name, picture_url: cityData.picture_url };
                });

                const tripsWithCityData = await Promise.all(cityDetailsPromises);
                setTrips(tripsWithCityData);
            } catch (error) {
                console.error("Error fetching trips: ", error);
                setError("Failed to load travel plans. Please try again later.");
            } finally {
                setLoading(false);
            }
        }

        if (user) {
            fetchUserTrips();
        } else {
            navigate('/signin');
        }
    }, [user, navigate]);

    const handleTripClick = (tripId) => {
        navigate(`/trips/${tripId}`);
    };

    if (loading) {
        return <p>Loading...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    if (!trips.length) {
        return <p>No travel plans available.</p>;
    }

    return (
        <>
            <div className="profile-container">
                <h2>Your Travel Plans</h2>
                <div className="travel-plans">
                    {trips.map((trip) => (
                        <div
                            key={trip.id}
                            className="travel-plan-card"
                            onClick={() => handleTripClick(trip.id)}
                            style={{ cursor: 'pointer' }}
                        >
                            <h5>Trip to {trip.city_name}</h5> 
                            <img src={trip.picture_url} alt={trip.city_name} width="300" />
                            <p>Start Date: {new Date(trip.start_date).toLocaleDateString()}</p>
                            <p>End Date: {new Date(trip.end_date).toLocaleDateString()}</p>
                        </div>
                    ))}
                </div>
            </div>
            <SmallFooter />
        </>
    );
}
