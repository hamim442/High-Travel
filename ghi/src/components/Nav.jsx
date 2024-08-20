import { NavLink } from 'react-router-dom'
import { useState } from 'react'

export default function Nav() {
    const [searchQuery, setSearchQuery] = useState('')

    const handleSearchChange = (event) => {
        setSearchQuery(event.target.value)
    }

    const handleSearchSubmit = (event) => {
        event.preventDefault()
        console.log('Search query:', searchQuery)
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
                        <form className="d-flex" onSubmit={handleSearchSubmit}>
                            <input
                                className="form-control me-2"
                                type="search"
                                placeholder="Search"
                                aria-label="Search"
                                value={searchQuery}
                                onChange={handleSearchChange}
                            />
                            <button className="btn btn-dark" type="submit">
                                Search
                            </button>
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
