import MadridHero from '../assets/MadridHero.jpg'
import './styles/MainPage.css'

export default function MainPage() {
    return (
        <div className="main-container">
            <div
                className="background"
                style={{ backgroundImage: `url(${MadridHero})` }}
            ></div>
            <div className="overlay"></div>
            <div className="content">
                <h1 className="display-4 fw-bold mb-4">
                    Explore the World with HighTravel
                </h1>
                <p className="lead">Your Adventure Starts Here</p>
                <button type="button" className="btn btn-success">
                    Create Your Next Plan
                </button>
            </div>
        </div>
    )
}
