import { useParams, useNavigate } from 'react-router-dom'
import { useEffect, useState } from 'react'
import useAuthService from '../hooks/useAuthService'

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
        <div className="container-fluid p-0">
            <div
                className="city-hero"
                style={{ backgroundImage: `url(${city.picture_url})` }}
            >
                <div className="city-watermark">
                    <h1 className="text-light">{city.name}</h1>
                </div>
            </div>
            <div className="city-description">
                <p>{city.description}</p>
                <button
                    className="btn btn-success"
                    onClick={handleCreatePlanClick}
                >
                    Create Your Plan
                </button>
            </div>
        </div>
    )
}
