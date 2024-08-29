import { useState, useEffect } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import AdventureJumbotron from './AdventureJumbotron'
import SmallFooter from './SmallFooter'
import './styles/Sign.css'

export default function CreateNewCity() {
    const [name, setName] = useState('')
    const [administrativeDivision, setAdministrativeDivision] = useState('')
    const [country, setCountry] = useState('')
    const [pictureUrl, setPictureUrl] = useState('')
    const [description, setDescription] = useState('')
    const [error, setError] = useState(null)
    const navigate = useNavigate()
    const location = useLocation()

    useEffect(() => {
        window.scrollTo(0, 0)

        async function checkAuth() {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/auth/authenticate`,
                { credentials: 'include' }
            )
            if (!response.ok) {
                navigate('/signin', { state: { from: location.pathname } })
            }
        }
        checkAuth()
    }, [navigate, location])

    async function checkCityExists(cityName, countryName) {
        try {
            const response = await fetch(
                `${
                    import.meta.env.VITE_API_HOST
                }/api/cities?search=${cityName}`,
                { credentials: 'include' }
            )
            const cities = await response.json()

            return cities.some(
                (city) =>
                    city.name.toLowerCase() === cityName.toLowerCase() &&
                    city.country.toLowerCase() === countryName.toLowerCase()
            )
        } catch (error) {
            console.error('Error checking city existence:', error)
            return false
        }
    }

    async function handleFormSubmit(e) {
        e.preventDefault()

        const cityExists = await checkCityExists(name, country)

        if (cityExists) {
            setError(
                'This city already exists in the database for the specified country.'
            )
            return
        }

        const cityData = {
            name,
            administrative_division: administrativeDivision,
            country,
            picture_url: pictureUrl,
            description,
        }

        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/cities`,
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(cityData),
                    credentials: 'include',
                }
            )

            if (response.ok) {
                const newCity = await response.json()
                navigate(`/city/${newCity.id}`)
            } else {
                throw new Error('Failed to create city')
            }
        } catch (error) {
            console.error('Error creating city:', error)
            setError('Failed to create city. Please try again.')
        }
    }

    return (
        <div
            className="container-fluid"
            style={{ height: '85vh', marginTop: '2rem' }}
        >
            <div className="row h-100">
                {/* Create New City Form */}
                <div className="col-md-6 d-flex flex-column justify-content-start pt-4">
                    <div className="w-75 mx-auto">
                        <form onSubmit={handleFormSubmit}>
                            <h2 className="mb-4">
                                Add a New HighTravel Destination
                            </h2>
                            {error && (
                                <div className="alert alert-danger">
                                    {error}
                                </div>
                            )}

                            <div className="form-group mb-3">
                                <label htmlFor="name">City Name</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="name"
                                    value={name}
                                    onChange={(e) => setName(e.target.value)}
                                    placeholder="Gotham City"
                                    required
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label htmlFor="administrativeDivision">
                                    Administrative Division
                                </label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="administrativeDivision"
                                    value={administrativeDivision}
                                    onChange={(e) =>
                                        setAdministrativeDivision(
                                            e.target.value
                                        )
                                    }
                                    placeholder="Gotham State"
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label htmlFor="country">Country</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="country"
                                    value={country}
                                    onChange={(e) => setCountry(e.target.value)}
                                    placeholder="United States"
                                    required
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label htmlFor="pictureUrl">Picture URL</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="pictureUrl"
                                    value={pictureUrl}
                                    onChange={(e) =>
                                        setPictureUrl(e.target.value)
                                    }
                                    placeholder="http://www.example.com/gotham.jpg"
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label htmlFor="description">Description</label>
                                <textarea
                                    className="form-control"
                                    id="description"
                                    value={description}
                                    onChange={(e) =>
                                        setDescription(e.target.value)
                                    }
                                    placeholder="Enter what you love about this destination"
                                />
                            </div>

                            <button
                                type="submit"
                                className="btn btn-primary w-100"
                            >
                                Add City
                            </button>
                        </form>
                    </div>
                </div>

                {/* Adventure Jumbotron */}
                <div className="col-md-6 p-0 h-100">
                    <AdventureJumbotron />
                </div>

                {/* Footer */}
                <SmallFooter />
            </div>
        </div>
    )
}
