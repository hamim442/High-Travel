import { useState } from 'react'
import { Navigate } from 'react-router-dom'
import useAuthService from '../hooks/useAuthService'
import AdventureJumbotron from './AdventureJumbotron'
import './styles/Sign.css'

export default function SignUpForm() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const { signup, user, error } = useAuthService()

    async function handleFormSubmit(e) {
        e.preventDefault()
        await signup({ username, password })
    }

    if (user) {
        return <Navigate to="/" />
    }

    return (
        <div
            className="container-fluid"
            style={{ height: '85vh', marginTop: '2rem' }}
        >
            <div className="row h-100">
                {/* Sign Up Form */}
                <div className="col-md-6 d-flex flex-column justify-content-start pt-4">
                    <div className="w-75 mx-auto">
                        <form onSubmit={handleFormSubmit}>
                            <h2 className="mb-4">Sign Up</h2>
                            {error && (
                                <div className="alert alert-danger">
                                    {error.message}
                                </div>
                            )}

                            <div className="form-group mb-3">
                                <label htmlFor="username">Username</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="username"
                                    value={username}
                                    onChange={(e) =>
                                        setUsername(e.target.value)
                                    }
                                    placeholder="Enter Username"
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label htmlFor="password">Password</label>
                                <input
                                    type="password"
                                    className="form-control"
                                    id="password"
                                    value={password}
                                    onChange={(e) =>
                                        setPassword(e.target.value)
                                    }
                                    placeholder="Enter Password"
                                />
                            </div>

                            <button
                                type="submit"
                                className="btn btn-primary w-100"
                            >
                                Sign Up
                            </button>
                        </form>
                    </div>
                </div>

                {/* Adventure Jumbotron */}
                <div className="col-md-6 p-0 h-100">
                    <AdventureJumbotron />
                </div>
            </div>
        </div>
    )
}
