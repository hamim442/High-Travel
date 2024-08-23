import { useParams, useNavigate } from 'react-router-dom'
import { useEffect, useState } from 'react'
import useAuthService from '../hooks/useAuthService'
import './styles/CityPage.css'

export default function CityPage() {
    const { cityId } = useParams()
    const { user } = useAuthService()
    const navigate = useNavigate()
    const [city, setCity] = useState(null)
    const [attractions, setAttractions] = useState([])
    const [hotels, setHotels] = useState([])
    const [restaurants, setRestaurants] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() => {
        async function fetchCityData() {
            setLoading(true)
            setError(null)
            try {
                const response = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/cities/${cityId}`
                )
                if (!response.ok) {
                    throw new Error('Failed to fetch city data')
                }
                const data = await response.json()
                setCity(data)

                if (data.name && data.country) {
                    await fetchTripAdvisorData(data.name, data.country)
                } else {
                    console.error('City data is incomplete:', data)
                    setError(
                        'City data is incomplete. Unable to fetch attractions.'
                    )
                }
            } catch (error) {
                console.error('Error fetching city data: ', error)
                setError('Failed to load city data. Please try again later.')
            } finally {
                setLoading(false)
            }
        }

        async function fetchTripAdvisorData(cityName, country) {
            try {
                const encodedCity = encodeURIComponent(cityName)
                const encodedCountry = encodeURIComponent(country)

                const responseAttractions = await fetch(
                    `${
                        import.meta.env.VITE_API_HOST
                    }/tripadvisor/attractions?city=${encodedCity}&country=${encodedCountry}`
                )
                if (!responseAttractions.ok) {
                    throw new Error('Failed to fetch attractions')
                }
                const attractionsData = await responseAttractions.json()
                setAttractions(attractionsData.slice(0, 5))

                const responseHotels = await fetch(
                    `${
                        import.meta.env.VITE_API_HOST
                    }/tripadvisor/hotels?city=${encodedCity}&country=${encodedCountry}`
                )
                if (!responseHotels.ok) {
                    throw new Error('Failed to fetch hotels')
                }
                const hotelsData = await responseHotels.json()
                setHotels(hotelsData.slice(0, 5))

                const responseRestaurants = await fetch(
                    `${
                        import.meta.env.VITE_API_HOST
                    }/tripadvisor/restaurants?city=${encodedCity}&country=${encodedCountry}`
                )
                if (!responseRestaurants.ok) {
                    throw new Error('Failed to fetch restaurants')
                }
                const restaurantsData = await responseRestaurants.json()
                setRestaurants(restaurantsData.slice(0, 5))
            } catch (error) {
                console.error('Error fetching TripAdvisor data:', error)
                setError(
                    'Failed to load attraction data. Please try again later.'
                )
            }
        }

        fetchCityData()
    }, [cityId])

    const handleCreatePlanClick = () => {
        if (user) {
            navigate('/create-your-travel')
        } else {
            navigate('/signin')
        }
    }

    if (loading) {
        return <p>Loading...</p>
    }

    if (error) {
        return <p>{error}</p>
    }

    if (!city) {
        return <p>No city data available.</p>
    }

    return (
        <div className="city-container">
            {/* Hero Section */}
            <div
                className="city-hero"
                style={{ backgroundImage: `url(${city.picture_url})` }}
            >
                <div className="city-header">{city.name}</div>
            </div>
            <div className="city-description">{city.description}</div>
            <button
                className="city-plan-button"
                onClick={handleCreatePlanClick}
            >
                Create Your Plan
            </button>

            {/* <div className="popular-destinations-container">
                <div className="popular-destinations-title">
                    <h3>Top 5 Attractions</h3>
                </div>
                <div className="card-container">
                    {attractions.length > 0 ? (
                        attractions.map((attraction, index) => (
                            <div
                                key={index}
                                className="card"
                                onClick={() =>
                                    window.open(
                                        attraction.details.web_url,
                                        '_blank'
                                    )
                                }
                            >
                                <img
                                    className="card-img-top"
                                    src={
                                        attraction.photo_url ||
                                        'placeholder.jpg'
                                    }
                                    alt={attraction.name}
                                />
                                <div className="card-body">
                                    <h5 className="card-title">
                                        {attraction.name}
                                    </h5>
                                    <p className="card-text">
                                        {attraction.details.description}
                                    </p>
                                </div>
                            </div>
                        ))
                    ) : (
                        <p>No attractions data available.</p>
                    )}
                </div>
            </div>

            <div className="popular-destinations-container">
                <div className="popular-destinations-title">
                    <h3>Top 5 Hotels</h3>
                </div>
                <div className="card-container">
                    {hotels.length > 0 ? (
                        hotels.map((hotel, index) => (
                            <div
                                key={index}
                                className="card"
                                onClick={() =>
                                    window.open(hotel.details.web_url, '_blank')
                                }
                            >
                                <img
                                    className="card-img-top"
                                    src={hotel.photo_url || 'placeholder.jpg'}
                                    alt={hotel.name}
                                />
                                <div className="card-body">
                                    <h5 className="card-title">{hotel.name}</h5>
                                    <p className="card-text">
                                        {hotel.details.description}
                                    </p>
                                </div>
                            </div>
                        ))
                    ) : (
                        <p>No hotels data available.</p>
                    )}
                </div>
            </div>

            <div className="popular-destinations-container">
                <div className="popular-destinations-title">
                    <h3>Top 5 Restaurants</h3>
                </div>
                <div className="card-container">
                    {restaurants.length > 0 ? (
                        restaurants.map((restaurant, index) => (
                            <div
                                key={index}
                                className="card"
                                onClick={() =>
                                    window.open(
                                        restaurant.details.web_url,
                                        '_blank'
                                    )
                                }
                            >
                                <img
                                    className="card-img-top"
                                    src={
                                        restaurant.photo_url ||
                                        'placeholder.jpg'
                                    }
                                    alt={restaurant.name}
                                />
                                <div className="card-body">
                                    <h5 className="card-title">
                                        {restaurant.name}
                                    </h5>
                                    <p className="card-text">
                                        {restaurant.details.description}
                                    </p>
                                </div>
                            </div>
                        ))
                    ) : (
                        <p>No restaurants data available.</p>
                    )}
                </div>
            </div> */}
        </div>
    )
}
