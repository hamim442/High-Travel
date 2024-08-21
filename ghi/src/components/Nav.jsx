import { NavLink, useNavigate } from 'react-router-dom'
import { useState } from 'react'

export default function Nav() {
    const [searchQuery, setSearchQuery] = useState('')
    const [searchResults, setSearchResults] = useState([])
    const navigate = useNavigate()

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
        setSearchQuery('')
        setSearchResults([])
        navigate(`/city/${city.id}`)
    }

    return (
        <nav
            className="navbar navbar-expand-lg"
            style={{ backgroundColor: '#fefae0' }}
        >
            <div className="container-fluid">
                <NavLink
                    className="navbar-brand"
                    to="/"
                    style={{
                        fontFamily: 'Helvetica, Arial, sans-serif',
                        fontWeight: 'bold',
                        color: '#212529',
                    }}
                >
                    HighTravel
                </NavLink>
                <button
                    className="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarNavDropdown"
                    aria-controls="navbarNavDropdown"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div
                    className="collapse navbar-collapse justify-content-between"
                    id="navbarNavDropdown"
                >
                    <div className="navbar-nav ms-auto me-auto">
                        <form className="d-flex">
                            <input
                                className="form-control me-2"
                                type="search"
                                placeholder="Search"
                                aria-label="Search"
                                value={searchQuery}
                                onChange={handleSearchChange}
                            />
                            <ul
                                className="list-group"
                                style={{ position: 'absolute', zIndex: 1000 }}
                            >
                                {searchResults.map((city) => (
                                    <li
                                        key={city.id}
                                        className="list-group-item"
                                        onClick={() => handleSearchSelect(city)}
                                    >
                                        {city.name},{' '}
                                        {city.administrative_division}
                                    </li>
                                ))}
                            </ul>
                        </form>
                    </div>
                    <ul className="navbar-nav">
                        <li className="nav-item">
                            <NavLink
                                className="nav-link fs-6"
                                to="/signin"
                                style={{ color: '#212529' }}
                            >
                                Sign In
                            </NavLink>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    )
}
