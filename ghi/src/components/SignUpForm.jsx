import { useState } from 'react'
import { Navigate } from 'react-router-dom'
import useAuthService from '../hooks/useAuthService'
import AdventureJumbotron from './AdventureJumbotron'
import SmallFooter from './SmallFooter'
import './styles/Sign.css'

export default function SignUpForm() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')
    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [profileImage, setProfileImage] = useState('')
    const { signup, user, error } = useAuthService()

    async function handleFormSubmit(e) {
        e.preventDefault()
        await signup({
            username,
            password,
            email,
            first_name: firstName,
            last_name: lastName,
            profile_image: profileImage,
        })
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
                {/* Sign In Form */}
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
                                    name="username"
                                    value={username}
                                    onChange={(e) =>
                                        setUsername(e.target.value)
                                    }
                                    placeholder="Enter Username"
                                    required
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label htmlFor="password">Password</label>
                                <input
                                    type="password"
                                    className="form-control"
                                    name="password"
                                    value={password}
                                    onChange={(e) =>
                                        setPassword(e.target.value)
                                    }
                                    placeholder="Enter Password"
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label htmlFor="email">Email</label>
                                <input
                                    type="email"
                                    className="form-control"
                                    name="email"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    placeholder="jane.doe@email.com"
                                    required
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label htmlFor="firstName">First Name</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    name="firstName"
                                    value={firstName}
                                    onChange={(e) =>
                                        setFirstName(e.target.value)
                                    }
                                    placeholder="Jane"
                                    required
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label htmlFor="lastName">Last Name</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    name="lastName"
                                    value={lastName}
                                    onChange={(e) =>
                                        setLastName(e.target.value)
                                    }
                                    placeholder="Doe"
                                    required
                                />
                            </div>

                            <div className="form-group mb-3">
                                <label htmlFor="profileImage">
                                    Profile Image URL
                                </label>
                                <input
                                    type="text"
                                    className="form-control"
                                    name="profileImage"
                                    value={profileImage}
                                    onChange={(e) =>
                                        setProfileImage(e.target.value)
                                    }
                                    placeholder="http://www.example.com/janedoe.jpg"
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
            {/* Footer */}
            <SmallFooter />
        </div>
    )
}
