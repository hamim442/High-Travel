import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import useAuthService from '../hooks/useAuthService'
import './SpinCity.css'

const SpinCity = ({ cities }) => {
    const { user } = useAuthService()
    const [spin, setSpin] = useState(false)
    const [selectedCities, setSelectedCities] = useState([null, null, null])
    const navigate = useNavigate

    useEffect(() => {
    if (!user) {
        navigate('/signin')
    }

    useEffect(() => {
        let interval
        if (spin) {
            interval = setInterval(() => {
                const randomCities = []
                while (randomCities.length < 3) {
                    const randomIndex = Math.floor(
                        Math.random() * cities.length
                    )
                    const city = cities[randomIndex]
                    if (!randomCities.includes(city)) {
                        randomCities.push(city)
                    }
                }
                setSelectedCities(randomCities)
            }, 100)
        }

        return () => clearInterval(interval)
    }, [spin, cities])

    useEffect(() => {
        const timer = setTimeout(() => {
            setSpin(false)
        }, 3000)

        return () => clearTimeout(timer)
    }, [])

    return (
        <div className="spin-container">
            {selectedCities.map((city, index) => (
                <div
                    key={index}
                    className={`city ${index === 1 ? 'winner' : ''}`}
                >
                    {city && <h2>{city.name}</h2>}
                </div>
            ))}
        </div>
    )
}

export default SpinCity
