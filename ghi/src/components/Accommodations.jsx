import { useState, useEffect } from 'react'
import { Form, Button, Row, Col } from 'react-bootstrap'
import { useNavigate, useParams } from 'react-router-dom'

const AccommodationForm = () => {
    const [formData, setFormData] = useState({
        address: '',
        city: '',
        state: '',
        zipCode: '',
        country: '',
        phone: '',
        email: '',
        checkInDate: '',
        checkOutDate: '',
        numberOfGuests: '',
        totalPrice: '',
        notes: '',
        stayId: '',
    })

    const [stays, setStays] = useState([])
    const navigate = useNavigate()
    const { tripid } = useParams()

    useEffect(() => {
        // Fetch stays from the backend
        const fetchStays = async () => {
            try {
                const response = await fetch('localhost:8000/api/stays/')
                if (!response.ok) {
                    throw new Error('Network response was not ok')
                }
                const staysData = await response.json()
                console.log('Fetched stays:', staysData) // Log fetched data
                setStays(staysData)
            } catch (error) {
                console.error('Error fetching stays:', error)
            }
        }

        fetchStays()
    }, [])

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        })
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (tripid) {
            await saveAccommodation({ ...formData, trip: tripid })
            navigate(`/trips/${tripid}`)
        } else {
            console.error('No tripid found')
        }
    }

    const handleSubmitAndAddAnother = async (e) => {
        e.preventDefault()
        if (tripid) {
            await saveAccommodation({ ...formData, trip: tripid })
            setFormData({
                address: '',
                city: '',
                state: '',
                zipCode: '',
                country: '',
                phone: '',
                email: '',
                checkInDate: '',
                checkOutDate: '',
                numberOfGuests: '',
                totalPrice: '',
                notes: '',
                stayId: '',
            })
        } else {
            console.error('No tripid found')
        }
    }

    const saveAccommodation = async (data) => {
        try {
            const response = await fetch('/api/accommodations', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })

            if (!response.ok) {
                throw new Error('Network response was not ok')
            }

            const result = await response.json()
            console.log('Accommodation saved:', result)
        } catch (error) {
            console.error('There was a problem with the save operation:', error)
        }
    }

    return (
        <Form>
            <Row className="mb-3">
                <Form.Group as={Col} controlId="formStay">
                    <Form.Label>Stay</Form.Label>
                    <Form.Control
                        as="select"
                        name="stayId"
                        value={formData.stayId}
                        onChange={handleChange}
                    >
                        <option value="">Select a stay</option>
                        {stays.map((stay) => (
                            <option key={stay.id} value={stay.id}>
                                {stay.name}
                            </option>
                        ))}
                    </Form.Control>
                </Form.Group>
            </Row>

            <Row className="mb-3">
                <Form.Group as={Col} controlId="formAddress">
                    <Form.Label>Address</Form.Label>
                    <Form.Control
                        type="text"
                        name="address"
                        placeholder="Enter address"
                        value={formData.address}
                        onChange={handleChange}
                    />
                </Form.Group>

                <Form.Group as={Col} controlId="formCity">
                    <Form.Label>City</Form.Label>
                    <Form.Control
                        type="text"
                        name="city"
                        placeholder="Enter city"
                        value={formData.city}
                        onChange={handleChange}
                    />
                </Form.Group>
            </Row>

            <Row className="mb-3">
                <Form.Group as={Col} controlId="formState">
                    <Form.Label>State or Province</Form.Label>
                    <Form.Control
                        type="text"
                        name="state"
                        placeholder="Enter state or province"
                        value={formData.state}
                        onChange={handleChange}
                    />
                </Form.Group>

                <Form.Group as={Col} controlId="formZipCode">
                    <Form.Label>Zip Code</Form.Label>
                    <Form.Control
                        type="text"
                        name="zipCode"
                        placeholder="Enter zip code"
                        value={formData.zipCode}
                        onChange={handleChange}
                    />
                </Form.Group>
            </Row>

            <Row className="mb-3">
                <Form.Group as={Col} controlId="formCountry">
                    <Form.Label>Country</Form.Label>
                    <Form.Control
                        type="text"
                        name="country"
                        placeholder="Enter country"
                        value={formData.country}
                        onChange={handleChange}
                    />
                </Form.Group>

                <Form.Group as={Col} controlId="formPhone">
                    <Form.Label>Phone</Form.Label>
                    <Form.Control
                        type="text"
                        name="phone"
                        placeholder="Enter phone number"
                        value={formData.phone}
                        onChange={handleChange}
                    />
                </Form.Group>
            </Row>

            <Row className="mb-3">
                <Form.Group as={Col} controlId="formEmail">
                    <Form.Label>Email</Form.Label>
                    <Form.Control
                        type="email"
                        name="email"
                        placeholder="Enter email"
                        value={formData.email}
                        onChange={handleChange}
                    />
                </Form.Group>

                <Form.Group as={Col} controlId="formGuests">
                    <Form.Label>Number of Guests</Form.Label>
                    <Form.Control
                        type="number"
                        name="numberOfGuests"
                        placeholder="Enter number of guests"
                        value={formData.numberOfGuests}
                        onChange={handleChange}
                    />
                </Form.Group>
            </Row>

            <Row className="mb-3">
                <Form.Group as={Col} controlId="formCheckInDate">
                    <Form.Label>Check-in Date</Form.Label>
                    <Form.Control
                        type="date"
                        name="checkInDate"
                        value={formData.checkInDate}
                        onChange={handleChange}
                    />
                </Form.Group>

                <Form.Group as={Col} controlId="formCheckOutDate">
                    <Form.Label>Check-out Date</Form.Label>
                    <Form.Control
                        type="date"
                        name="checkOutDate"
                        value={formData.checkOutDate}
                        onChange={handleChange}
                    />
                </Form.Group>
            </Row>

            <Row className="mb-3">
                <Form.Group as={Col} controlId="formTotalPrice">
                    <Form.Label>Total Price</Form.Label>
                    <Form.Control
                        type="number"
                        name="totalPrice"
                        placeholder="Enter total price"
                        value={formData.totalPrice}
                        onChange={handleChange}
                    />
                </Form.Group>
            </Row>

            <Form.Group className="mb-3" controlId="formNotes">
                <Form.Label>Notes</Form.Label>
                <Form.Control
                    as="textarea"
                    name="notes"
                    rows={3}
                    placeholder="Enter any additional notes"
                    value={formData.notes}
                    onChange={handleChange}
                />
            </Form.Group>

            <Button variant="primary" onClick={handleSubmit}>
                Submit
            </Button>

            <Button
                variant="secondary"
                className="ms-2"
                onClick={handleSubmitAndAddAnother}
            >
                Submit and add another accommodation
            </Button>
        </Form>
    )
}

export default AccommodationForm
