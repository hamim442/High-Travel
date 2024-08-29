import { useEffect, useState } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import AdventureJumbotron from './AdventureJumbotron'
import SmallFooter from './SmallFooter'
import './styles/CreateTravelPlan.css'

export default function CreateTravelPlan() {
    const location = useLocation()
    const initialCity = location.state?.city || null
    const [destination, setDestination] = useState('')
    const [selectedCity, setSelectedCity] = useState(null)
    const [fromDate, setFromDate] = useState('')
    const [toDate, setToDate] = useState('')
    const [searchResults, setSearchResults] = useState([])
    const [error, setError] = useState(null)
    const navigate = useNavigate()

    // user authenticated?
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

    // this runs if we got here from clicking on Create Plan in a CityPage
    useEffect(() => {
        if (initialCity) {
            setDestination(
                `${initialCity.name}, ${initialCity.administrative_division}, ${initialCity.country}`
            )
            setSelectedCity(initialCity)
        }
    }, [initialCity])

    // this handles when you type in destination box
    const handleSearchChange = async (event) => {
        const searchQuery = event.target.value
        setDestination(searchQuery)
        setSelectedCity(null)
        if (searchQuery.length > 2) {
            try {
                const response = await fetch(
                    `${
                        import.meta.env.VITE_API_HOST
                    }/api/cities?search=${searchQuery}`,
                    { credentials: 'include' }
                )
                if (!response.ok) {
                    throw new Error('Failed to fetch search results')
                }
                const data = await response.json()
                setSearchResults(data)
            } catch (error) {
                console.error('Error fetching search results:', error)
                setError('Failed to fetch search results. Please try again.')
            }
        } else {
            setSearchResults([])
        }
    }

    // this is what happens when you click on a destination result
    const handleSearchSelect = (city) => {
        setDestination(
            `${city.name}, ${city.administrative_division}, ${city.country}`
        )
        setSelectedCity(city)
        setSearchResults([])
    }

    // this handles the creation of the travel plan
    async function handleSubmit(event) {
        event.preventDefault()
        setError(null)

        if (!selectedCity) {
            setError(
                'Please select a valid destination from the search results.'
            )
            return
        }

        const tripData = {
            city_id: selectedCity.id,
            start_date: new Date(fromDate).toISOString(),
            end_date: new Date(toDate).toISOString(),
        }

        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/trips/`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(tripData),
                    credentials: 'include',
                }
            )

            if (!response.ok) {
                const errorData = await response.json()
                throw new Error(errorData.detail || 'Failed to create trip')
            }

            navigate('/trips')
        } catch (error) {
            console.error('Error creating trip:', error)
            setError('Failed to create trip. Please try again.')
            if (error.message === 'Authentication required') {
                navigate('/signin')
            }
        }
    }

    return (
        <div
            className="container-fluid"
            style={{ height: '85vh', marginTop: '2rem' }}
        >
            <div className="row h-100">
                {/* Create Travel Plan Form */}
                <div className="col-md-6 d-flex flex-column justify-content-start pt-4">
                    <div className="w-75 mx-auto">
                        <form onSubmit={handleSubmit}>
                            <h2 className="mb-4">Create Travel Plan</h2>
                            {error && (
                                <div
                                    className="alert alert-danger"
                                    role="alert"
                                >
                                    {error}
                                </div>
                            )}
                            {/* This is where you search for a city */}
                            <div className="form-group mb-3">
                                <label htmlFor="destination">Destination</label>
                                <div className="search-container">
                                    <input
                                        type="text"
                                        className={`form-control ${
                                            selectedCity ? 'is-valid' : ''
                                        }`}
                                        id="destination"
                                        value={destination}
                                        onChange={handleSearchChange}
                                        placeholder="Enter destination"
                                        required
                                    />
                                    {/* This shows the search results */}
                                    {searchResults.length > 0 && (
                                        <ul className="list-group search-results">
                                            {searchResults.map((city) => (
                                                <li
                                                    key={city.id}
                                                    className="list-group-item search-result-item"
                                                    onClick={() =>
                                                        handleSearchSelect(city)
                                                    }
                                                >
                                                    {city.name},{' '}
                                                    {
                                                        city.administrative_division
                                                    }
                                                    , {city.country}
                                                </li>
                                            ))}
                                        </ul>
                                    )}
                                </div>
                            </div>

                            {/* This is where you pick your travel dates */}
                            <div className="form-group mb-3">
                                <label htmlFor="fromDate">From Date</label>
                                <input
                                    type="date"
                                    className="form-control"
                                    id="fromDate"
                                    value={fromDate}
                                    onChange={(e) =>
                                        setFromDate(e.target.value)
                                    }
                                    required
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label htmlFor="toDate">To Date</label>
                                <input
                                    type="date"
                                    className="form-control"
                                    id="toDate"
                                    value={toDate}
                                    onChange={(e) => setToDate(e.target.value)}
                                    required
                                />
                            </div>

                            {/* This button submits the form */}
                            <button
                                type="submit"
                                className="btn btn-primary w-100"
                            >
                                Create Travel Plan
                            </button>
                        </form>
                    </div>
                </div>

                {/* Adventure Jumbotron component */}
                <div className="col-md-6 p-0 h-100">
                    <AdventureJumbotron />
                </div>

                {/* Footer */}
                <SmallFooter />
            </div>
        </div>
    )
}
