import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from 'react'
import useAuthService from '../hooks/useAuthService'
import './styles/RandomDestinations.css'
import SmallFooter from './SmallFooter'


export default function UserTravelPlans() {
    const { user } = useAuthService();
    const navigate = useNavigate();
    const [trips, setTrips] = useState([]);
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() => {
        async function fetchUserTrips() {
            setLoading(true);
            setError(null)

            try {
                const userTripResponse = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/user-trip/${user.id}`,
                    
                );

                if(!userTripResponse.ok) {
                    throw new Error("Failed to fetch user trips")
                }

                const userTrips = await userTripResponse.json();

                const tripDetailsPromises = userTrips.map(({ trip_id }) =>
                   fetch(`${import.meta.env.VITE_API_HOST}/api/trips/${trip_id}`)
                    .then((response) => {
                        if (response.ok) {
                            throw new Error("Failed to fetch trip details")
                        }
                        return response.json()
                    })
            );
            const tripsData = await Promise.all(tripDetailsPromises)

            setTrips(tripsData)
            } catch (error) {
                console.error("Error fetching trips: ", error)
                setError("Failed to load travel plans. Please try again later.")
            } finally {
                setLoading(false)
            }
        }

        if (user) {
            fetchUserTrips();
        } else {
            navigate('/signin')
        }
     }, [user, navigate])

    const handleTripClick = (tripId) => {
        navigate(`/trips/${tripId}`);
     }


    if (loading) {
        return <p>Loading...</p>
    }

    if (error) {
        return <p>{error}</p>
    }

    if(!trips.length) {
        return <p>NO travel plan available </p>
    }

    return (
        <>
            <div className="profile-container">
                <h2>Your Travel Plans</h2>
                <div className="travel-plans">
                    {trips.map((trip) => (
                        <div
                            key={trip.id} // Unique key for each trip for efficient rendering
                            className="travel-plan-card"
                            onClick={() => handleTripClick(trip.id)} // Make the card clickable
                            style={{ cursor: 'pointer' }} // Add a pointer cursor on hover to indicate it's clickable
                        >
                            <h5>Trip to {trip.city_id}</h5> {/* Display city ID or you may want to fetch city name instead */}
                            <p>Start Date: {new Date(trip.start_date).toLocaleDateString()}</p> {/* Format the start date */}
                            <p>End Date: {new Date(trip.end_date).toLocaleDateString()}</p> {/* Format the end date */}
                        </div>
                    ))}
                </div>
            </div>
            <SmallFooter /> 
        </>
    );
}





