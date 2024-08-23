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

    useEffect(() => {
        async function fetchCityData() {
            try {
                const response = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/cities/${cityId}`
                )
                const data = await response.json()
                setCity(data)

                fetchTripAdvisorData(data.name, data.country_name)
            } catch (error) {
                console.error('Error fetching city data: ', error)
            }
        }

        async function fetchTripAdvisorData(cityName, countryName) {
            try {
                const responseAttractions = await fetch(
                    `/api/tripadvisor/attractions?city=${cityName}&country=${countryName}`
                )
                const attractionsData = await responseAttractions.json()
                setAttractions(attractionsData.slice(0, 5))

                const responseHotels = await fetch(
                    `/api/tripadvisor/hotels?city=${cityName}&country=${countryName}`
                )
                const hotelsData = await responseHotels.json()
                setHotels(hotelsData.slice(0, 5))

                const responseRestaurants = await fetch(
                    `/api/tripadvisor/restaurants?city=${cityName}&country=${countryName}`
                )
                const restaurantsData = await responseRestaurants.json()
                setRestaurants(restaurantsData.slice(0, 5))
            } catch (error) {
                console.error('Error fetching TripAdvisor data:', error)
            }
        }

        fetchCityData()
    }, [cityId])

    const handleCreatePlanClick = () => {
        if (user) {
            navigate('/create-your-travel') // authenticated redirects to Create Plan page
        } else {
            navigate('/signin') // Not authenticated redirects to Sign-in page
        }
    }

    if (!city) {
        return <p>Loading...</p>
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

            {/* Attractions */}
            <div className="popular-destinations-container">
                <div className="popular-destinations-title">
                    <h3>Top 5 Attractions</h3>
                </div>
                <div className="card-container">
                    {attractions.map((attraction, index) => (
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
                                src={attraction.photo_url || 'placeholder.jpg'}
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
                    ))}
                </div>
            </div>

            {/* Hotels */}
            <div className="popular-destinations-container">
                <div className="popular-destinations-title">
                    <h3>Top 5 Hotels</h3>
                </div>
                <div className="card-container">
                    {hotels.map((hotel, index) => (
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
                    ))}
                </div>
            </div>

            {/* Restaurants */}
            <div className="popular-destinations-container">
                <div className="popular-destinations-title">
                    <h3>Top 5 Restaurants</h3>
                </div>
                <div className="card-container">
                    {restaurants.map((restaurant, index) => (
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
                                src={restaurant.photo_url || 'placeholder.jpg'}
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
                    ))}
                </div>
            </div>
        </div>
    )
}
