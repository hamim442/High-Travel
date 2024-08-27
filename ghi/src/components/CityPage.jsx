import { useParams, useNavigate } from 'react-router-dom'
import { useEffect, useState } from 'react'
import useAuthService from '../hooks/useAuthService'
import SmallFooter from './SmallFooter'
import './styles/CityPage.css'

export default function CityPage() {
    const { cityId } = useParams()
    const { user } = useAuthService()
    const navigate = useNavigate()
    const [city, setCity] = useState(null)
    const [stays, setStays] = useState([])
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

                const staysResponse = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/stays`
                )
                if (!response.ok) {
                    throw new Error('Failed to fetch stays data')
                }
                const staysData = await staysResponse.json()

                const shuffledStays = staysData.sort(() => 0.5 - Math.random())
                setStays(shuffledStays.slice(0, 5))
            } catch (error) {
                console.error('Error fetching city data: ', error)
                setError('Failed to load city data. Please try again later.')
            } finally {
                setLoading(false)
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
        <>
            {/* Hero Section */}
            <div className="city-container">
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
            </div>

            {/* Stays Section */}
            <div className="stays-container">
                <div>
                    <h2>Stay Recommendations</h2>
                    <div className="stays">
                        {stays.map((stay) => (
                            <div key={stay.id} className="stays-id">
                                <img
                                    src={stay.logo_picture_url}
                                    alt={stay.name}
                                    className="stay-image"
                                />
                                <p className="stays-name">{stay.name}</p>
                            </div>
                        ))}
                    </div>
                </div>
            </div>

            {/* Footer */}
            <SmallFooter />
        </>
    )
}
