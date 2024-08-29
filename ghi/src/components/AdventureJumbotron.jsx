import { useState, useEffect } from 'react'
import './styles/AdventureJumbotron.css'

const imageUrls = [
    'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/12/09/7b/02/at-michelin-starred-aroma.jpg',
    'https://media.architecturaldigest.com/photos/57ad893acfc37bc171ad8082/16:9/w_2560%2Cc_limit/madrid-travel-guide.jpg',
    'https://cdn.britannica.com/38/242638-050-D96EB78F/Buckingham-Palace-Victoria-Memorial-Tulips-London-England.jpg',
    'https://www.hotelpalomar-philadelphia.com/images/1700-960/downtown-philly-i-stock-680820188-7b7c9cf6.jpg',
    'https://www.exp1.com/blog/wp-content/uploads/sites/7/2015/10/High-Line-1.jpg',
]

export default function AdventureJumbotron() {
    const [imageUrl, setImageUrl] = useState('')

    useEffect(() => {
        const randomIndex = Math.floor(Math.random() * imageUrls.length)
        setImageUrl(imageUrls[randomIndex])
    }, [])

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
