import { NavLink, useNavigate } from 'react-router-dom'
import { useState, useEffect } from 'react'
import useAuthService from '../hooks/useAuthService'
import './styles/Nav.css'

export default function Nav() {
    const [searchQuery, setSearchQuery] = useState('')
    const [searchResults, setSearchResults] = useState([])
    const navigate = useNavigate()
    const { user, signout, isLoggedIn } = useAuthService()

    // added this useEffect to handle burger functionality
    useEffect(() => {
        const handleResize = () => {
            if (window.innerWidth > 991) {
                const navbarCollapse =
                    document.getElementById('navbarNavDropdown')
                if (
                    navbarCollapse &&
                    navbarCollapse.classList.contains('show')
                ) {
                    navbarCollapse.classList.remove('show')
                }
            }
        }
        window.addEventListener('resize', handleResize)
        return () => {
            window.removeEventListener('resize', handleResize)
        }
    }, [])

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

    const handleLogout = async () => {
        await signout()
        navigate('/')
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
                        <form
                            className="d-flex search-container"
                            style={{ flexGrow: 1, maxWidth: '300px' }}
                        >
                            <input
                                className="form-control me-2"
                                type="search"
                                placeholder="Search"
                                aria-label="Search"
                                value={searchQuery}
                                onChange={handleSearchChange}
                            />
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
                                            {city.administrative_division},{' '}
                                            {city.country}
                                        </li>
                                    ))}
                                </ul>
                            )}
                        </form>
                    </div>

                    <ul className="navbar-nav align-items-center">
                        {' '}
                        {isLoggedIn ? (
                            <>
                                <li className="nav-item">
                                    <NavLink
                                        to="/profile"
                                        className="nav-link fs-6"
                                        style={{
                                            color: '#212529',
                                            textDecoration: 'none',
                                        }}
                                    >
                                        {user.username}
                                    </NavLink>
                                </li>
                                <li className="nav-item">
                                    <button
                                        className="nav-link fs-6 btn btn-link"
                                        onClick={handleLogout}
                                        style={{ color: '#212529' }}
                                    >
                                        Logout
                                    </button>
                                </li>
                            </>
                        ) : (
                            <>
                                <li className="nav-item">
                                    <NavLink
                                        className="nav-link fs-6"
                                        to="/signin"
                                        style={{ color: '#212529' }}
                                    >
                                        Sign In
                                    </NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink
                                        className="nav-link fs-6"
                                        to="/signup"
                                        style={{ color: '#212529' }}
                                    >
                                        Sign Up
                                    </NavLink>
                                </li>
                            </>
                        )}
                    </ul>
                </div>
            </div>
        </nav>
    )
}
