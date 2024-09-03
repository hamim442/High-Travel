import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import useAuthService from '../hooks/useAuthService'

function EditUserProfile() {
    const { user, update } = useAuthService()
    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [profileImage, setProfileImage] = useState('')
    const navigate = useNavigate()

    useEffect(() => {
        if (!user) {
            navigate('/signin')
        } else {
            setFirstName(user.first_name || '')
            setLastName(user.last_name || '')
            setProfileImage(user.profile_image || '')
        }
    }, [user, navigate])

    const handleEdit = async (e) => {
        e.preventDefault()
        try {
            if (user) {
                update({
                    first_name: firstName,
                    last_name: lastName,
                    profile_image: profileImage,
                })
                navigate('/profile')
            }
        } catch (e) {
            console.error('Profile update failed', e)
        }
    }

    return (
        <div>
            <h1>Edit Profile</h1>
            <div>
                <p>Username: {user?.username}</p>
                <p>Email: {user?.email}</p>
            </div>
            <form onSubmit={handleEdit}>
                <div>
                    <label htmlFor="firstName">First Name</label>
                    <input
                        type="text"
                        id="firstName"
                        name="firstName"
                        value={firstName}
                        onChange={(e) => setFirstName(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="lastName">Last Name</label>
                    <input
                        type="text"
                        id="lastName"
                        name="lastName"
                        value={lastName}
                        onChange={(e) => setLastName(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="profileImage">Image URL</label>
                    <input
                        type="text"
                        id="profileImage"
                        name="profileImage"
                        value={profileImage}
                        onChange={(e) => setProfileImage(e.target.value)}
                    />
                </div>
                <button type="submit">Update Profile</button>
            </form>
        </div>
    )
}

export default EditUserProfile
