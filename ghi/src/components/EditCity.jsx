import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'

export default function EditCity() {
    const { cityId, tripId } = useParams()
    const navigate = useNavigate()

    const [cityData, setCityData] = useState({
        name: '',
        administrative_division: '',
        country: '',
        picture_url: '',
        description: '',
    })

    useEffect(() => {
        const fetchCity = async () => {
            try {
                const response = await fetch(
                    `http://localhost:8000/api/cities/${cityId}`
                )
                if (!response.ok) {
                    throw new Error('Cannot fetch City')
                }
                const city = await response.json()
                setCityData({
                    name: city.name,
                    administrative_division: city.administrative_division,
                    country: city.country,
                    picture_url: city.picture_url,
                    description: city.description,
                })
            } catch (e) {
                console.error('Fetch city details error', e)
            }
        }
        fetchCity()
    }, [cityId])

    const handleChange = (e) => {
        const { id, value } = e.target
        setCityData({
            ...cityData,
            [id]: value,
        })
    }

    const handleEdit = (e) => {
        e.preventDefault()

        const dataEdit = {
            ...cityData,
            trip_id: tripId,
            city_id: cityId,
        }

        console.log("Data to edit", dataEdit)

        try {
            const response = await fetch(`http://localhost:8000/api/cities/${cityId}`,
                {
                    method:'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(dataEdit),
                }
            )
            if (!response.ok) {
                const fail = await response.json()
                throw new Error(`Failed to updated City: ${fail.message || response.statusText}`)

            }
            navigate(-1)
        } catch (error) {
            console.error('error', error)
        }
    }
    return (
        <form onSubmit={handleEdit}>
                        <div className="mb-3">
                <h2>Edit Train Ride</h2>
            </div>
            <div className="mb-3">
                <label>Name:</label>
                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    className="form-control"
                    required
                />
            </div>
        </form>
    )
}
