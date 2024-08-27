import './styles/MainPage.css'
import MadridHero from '../assets/MadridHero.jpg'
import BigFooter from './BigFooter'
import RandomDestinations from './RandomDestinations'

export default function MainPage() {
    return (
        <div className="main-container">
            {/* Hero Section */}
            <div
                className="jumbotron jumbotron-fluid hero-section"
                style={{ backgroundImage: `url(${MadridHero})` }}
            >
                <div className="container">
                    <div className="hero-text-container">
                        <h1 className="hero-text">
                            Your next adventure starts here
                        </h1>
                    </div>
                    <p className="lead">
                        <button className="btn btn-success btn-md">
                            Create Your Next Plan
                        </button>
                    </p>
                </div>
            </div>

            {/* Random Destinations */}
            <RandomDestinations />

            {/* Footer */}
            <BigFooter />
        </div>
    )
}
