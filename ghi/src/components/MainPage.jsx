// import MadridHero from '/assets/HeroImages/MadridHero.jpg'

export default function MainPage() {
    const containerStyle = {
        position: 'relative',
        height: '100vh',
        width: '100%',
        overflow: 'hidden',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        color: '#FFFFFF',
        textShadow: '1px 1px 3px rgba(0,0,0,0.7)',
    }

    const backgroundStyle = {
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        // backgroundImage: `url(${MadridHero})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        zIndex: 0,
    }

    const overlayStyle = {
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.5)', // black translucent overlay
        zIndex: 1,
    }

    const contentStyle = {
        padding: '2rem',
        textAlign: 'center',
        zIndex: 2,
    }

    return (
        <div style={containerStyle}>
            <div style={backgroundStyle}></div>
            <div style={overlayStyle}></div>
            <div style={contentStyle}>
                <h1 className="display-4 fw-bold mb-4">
                    Explore the World with High Travel
                </h1>
                <p className="lead">Your Adventure Starts Here</p>
                <button type="button" className="btn btn-success">
                    Create Your Next Plan
                </button>
            </div>
        </div>
    )
}
