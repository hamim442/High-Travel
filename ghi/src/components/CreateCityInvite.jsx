import { useNavigate } from 'react-router-dom'
import './styles/CreateCityInvite.css'

export default function CreateCityInvitation() {
    const navigate = useNavigate()

    const handleAddCityClick = () => {
        navigate('/create-city')
    }

    return (
        <div className="create-city-invitation-container">
            <div className="create-city-invitation-title">
                <h3>The city you would like to visit is not here?</h3>
            </div>
            <div className="create-city-invitation-text">
                <p>Add it to our database and contribute to the community!</p>
                <button
                    className="btn btn-primary"
                    onClick={handleAddCityClick}
                >
                    Add city to our platform
                </button>
            </div>
        </div>
    )
}
