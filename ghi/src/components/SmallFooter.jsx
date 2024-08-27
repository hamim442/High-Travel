import './styles/Footer.css'

export default function SmallFooter() {
    return (
        <footer className="bigfoot bg-body-tertiary text-center">
            {/* Grid container */}
            <div className="container p-4"></div>

            {/* Copyright */}
            <div
                className="text-center p-3"
                style={{ backgroundColor: 'rgba(0, 0, 0, 0.05)' }}
            >
                © 2024 Copyright: HighTravel.com
            </div>
        </footer>
    )
}
