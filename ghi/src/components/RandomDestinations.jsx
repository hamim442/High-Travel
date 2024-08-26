import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import './styles/RandomDestinations.css'

export default function RandomDestinations() {
    const [popularDestinations, setPopularDestinations] = useState([])
    const navigate = useNavigate()

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_HOST}/api/cities/random`)
            .then((response) => response.json())
            .then((data) => setPopularDestinations(data))
            .catch((err) =>
                console.error('Failed to fetch popular destinations', err)
            )
    }, [])

    const handleCityClick = (cityId) => {
        navigate(`/city/${cityId}`)
    }

    return (
        <div className="random-destinations-container">
            <div className="random-destinations-title">
                <h3>Popular Destinations</h3>
            </div>
            <div className="card-container">
                {popularDestinations.map((city) => (
                    <div
                        className="card"
                        key={city.id}
                        onClick={() => handleCityClick(city.id)}
                    >
                        <img
                            className="card-img-top"
                            src={city.picture_url}
                            alt={city.name}
                        />
                        <div className="card-body">
                            <h5 className="card-title">{city.name}</h5>
                            <p className="card-text">{city.description}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}
