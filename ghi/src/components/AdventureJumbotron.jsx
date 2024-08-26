import './styles/AdventureJumbotron.css'

export default function AdventureJumbotron() {
    const imageUrl =
        'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/12/09/7b/02/at-michelin-starred-aroma.jpg'

    return (
        <div
            className="adventure-jumbotron"
            style={{ backgroundImage: `url(${imageUrl})` }}
        >
            <div className="hero-text-container">
                <h1 className="hero-text">Your adventure starts here</h1>
            </div>
        </div>
    )
}
