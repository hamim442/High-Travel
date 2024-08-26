import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import './styles/CityPage.css'

export default function CreateTravelPlansForm() {
    const [date, setDate] = useState('')
    const [travelers, setTravelers] = useState(1)
    const [searchQuery, setSearchQuery] = useState('')
    const [searchResults, setSearchResults] = useState([])
    const [cost, setCost] = useState(0)
    const [total, setTotal] = useState(0)
    const navigate = useNavigate()

    useEffect(() => {
        setTotal(cost * travelers)
    }, [cost, travelers])

    const handleSearchChange = async (event) => {
        setSearchQuery(event.target.value)
        if (event.target.value.length > 2) {
            try {
                const response = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/cities?search=${
                        event.target.value
                    }`
                )
                const data = await response.json()
                setSearchResults(data)
            } catch (error) {
                console.error('Error fetching search results:', error)
            }
        } else {
            setSearchResults([])
        }
    }

    const handleSearchSelect = (city) => {
        setSearchQuery(city.name)
        setSearchResults([])
    }

    async function handleSubmit(event) {
        event.preventDefault()
        const data = {
            city: searchQuery,
            date,
            travelers,
            cost,
            total,
        }
        const fetchConfig = {
            method: 'POST',
            body: JSON.stringify(data),
            headers: { 'Content-Type': 'application/json' },
        }
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/api/trips`,
                fetchConfig
            )
            if (response.ok) {
                navigate('/trips')
            } else {
                console.error('Create trip error', response.statusText)
            }
        } catch (error) {
            console.error('Form submit error', error)
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="city">City</label>
                <input
                    type="text"
                    id="city"
                    className="form-control"
                    value={searchQuery}
                    onChange={handleSearchChange}
                    placeholder="Type Available City"
                    required
                />
                {searchResults.length > 0 && (
                    <ul className="list-group search-results">
                        {searchResults.map((city) => (
                            <li
                                key={city.id}
                                className="list-group-item search-result-item"
                                onClick={() => handleSearchSelect(city)}
                            >
                                {city.name}, {city.administrative_division},{' '}
                                {city.country}
                            </li>
                        ))}
                    </ul>
                )}
            </div>
            <div className="form-group">
                <label htmlFor="date">Travel Date</label>
                <input
                    type="date"
                    id="date"
                    className="form-control"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="travelers">Number of Travelers</label>
                <input
                    type="number"
                    id="travelers"
                    className="form-control"
                    value={travelers}
                    onChange={(e) => setTravelers(Number(e.target.value))}
                    min="1"
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="cost">Individual Cost</label>
                <input
                    type="number"
                    id="cost"
                    className="form-control"
                    value={cost}
                    onChange={(e) => setCost(Number(e.target.value))}
                    min="0"
                    required
                />
            </div>
            <div className="form-group">
                <strong>Total Cost: ${total}</strong>
            </div>
            <button type="submit" className="btn btn-primary">
                Create Travel Plan
            </button>
        </form>
    )
}
