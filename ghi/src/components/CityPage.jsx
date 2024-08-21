import { useParams, useNavigate } from 'react-router-dom'
import { useEffect, useState } from 'react'
import useAuthService from '../hooks/useAuthService'
import './styles/CityPage.css'

export default function CityPage() {
    const { cityId } = useParams()
    const { user } = useAuthService()
    const navigate = useNavigate()
    const [city, setCity] = useState(null)

    useEffect(() => {
        async function fetchCityData() {
            try {
                const response = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/cities/${cityId}`
                )
                const data = await response.json()
                setCity(data)
            } catch (error) {
                console.error('Error fetching city data: ', error)
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
    )
}
