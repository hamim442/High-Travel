import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import useAuthService from '../hooks/useAuthService'

export default function UserProfileInfo() {
    const navigate = useNavigate()
    const { user } = useAuthService()
    const [profile, setProfile] = useState({
        id: '',
        username: '',
        email: '',
        first_name: '',
        last_name: '',
        profile_image: '',
    })

    useEffect(() => {
        async function fetchProfile() {
            if (user) {
                setProfile(user)
            } else {
                navigate('/signin')
            }
        }
        fetchProfile()
    }, [user, navigate])

    const handleCreatePlan = () => {
        // It would probably be better if the CreateTravelPlan page handled this,
        // then you wouldn't need this if statement here.
        if (user) {
            navigate('/create')
        } else {
            navigate('/signin')
        }
    }
    const handleEditProfile = () => {
        if (user) {
            navigate('/editprofile')
        } else {
            navigate('/signin')
        }
    }

    return (
        <>
            <div className="row d-flex justify-content-center">
                <div className="col col-md-9 col-lg-7 col-xl-6">
                    <div className="card">
                        <div className="card-body p-4">
                            <div className="d-flex">
                                <div className="flex-shrink-0">
                                    <img
                                        src={profile.profile_image}
                                        alt="Generic placeholder image"
                                        className="img-fluid"
                                    />
                                </div>
                                <div className="flex-grow-1 ms-3">
                                    <h5 className="mb-1">
                                        {profile.first_name} {profile.last_name}
                                    </h5>
                                    <p className="mb-2 pb-1">
                                        {profile.username}
                                    </p>
                                    <div className="d-flex justify-content-start rounded-3 p-2 mb-2 bg-body-tertiary">
                                        <div>
                                            <p className="small text-muted mb-1">
                                                Email
                                            </p>
                                            <p className="mb-0">
                                                {profile.email}
                                            </p>
                                        </div>
                                    </div>
                                    <div className="d-flex pt-1">
                                        <button
                                            type="button"
                                            data-mdb-button-init
                                            data-mdb-ripple-init
                                            className="btn btn-outline-primary me-1 flex-grow-1"
                                            onClick={handleEditProfile}
                                        >
                                            Edit Profile
                                        </button>
                                        <button
                                            type="button"
                                            data-mdb-button-init
                                            data-mdb-ripple-init
                                            className="btn btn-primary flex-grow-1"
                                            onClick={handleCreatePlan}
                                        >
                                            Create Plan
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
