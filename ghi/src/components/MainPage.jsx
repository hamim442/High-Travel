import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import './styles/MainPage.css'
import MadridHero from '../assets/MadridHero.jpg'

export default function MainPage() {
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
        <div className="main-container">
            <div
                className="jumbotron jumbotron-fluid hero-section"
                style={{ backgroundImage: `url(${MadridHero})` }}
            >
                <div className="container">
                    <div className="hero-text-container">
                        <h1 className="hero-text">
                            Your next adventure starts here
                        </h1>
                    </div>
                    <p className="lead">
                        <button className="btn btn-success btn-md">
                            Create Your Next Plan
                        </button>
                    </p>
                </div>
            </div>

            <div className="popular-destinations-container">
                <div className="popular-destinations-title">
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
        </div>
    )
}
