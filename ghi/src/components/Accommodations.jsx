import { useState, useEffect } from 'react'
import { Form, Button, Row, Col } from 'react-bootstrap'
import { useNavigate, useParams } from 'react-router-dom'

const AccommodationForm = () => {
    const [formData, setFormData] = useState({
        address: '',
        city: '',
        state_province: '',
        zip_code: '',
        country: '',
        phone: '',
        email: '',
        check_in_date: '',
        check_out_date: '',
        number_of_guests: '',
        total_price: '',
        notes: '',
        stays_id: '',
    })

    const [stays, setStays] = useState([])
    const navigate = useNavigate()
    const { tripid } = useParams()

    useEffect(() => {
        const fetchStays = async () => {
            try {
                const response = await fetch(
                    `${import.meta.env.VITE_API_HOST}/api/stays/`
                )
                const staysData = await response.json()
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

    const convertToDateTime = (dateStr) => {
        return dateStr ? `${dateStr}T00:00:00Z` : null
    }

    const handleSubmit = async (e) => {
        e.preventDefault()

        const dataToSubmit = {
            stays_id: formData.stays_id ? parseInt(formData.stays_id) : null,
            address: formData.address,
            city: formData.city,
            state_province: formData.state_province,
            zip_code: formData.zip_code,
            country: formData.country,
            phone: formData.phone,
            email: formData.email,
            check_in_date: convertToDateTime(formData.check_in_date),
            check_out_date: convertToDateTime(formData.check_out_date),
            number_of_guests: formData.number_of_guests
                ? parseInt(formData.number_of_guests, 10)
                : null,
            total_price: formData.total_price
                ? parseFloat(formData.total_price)
                : null,
            notes: formData.notes,
            trip_id: parseInt(tripid, 10),
        }

        console.log('Data being sent:', dataToSubmit)

        try {
            const response = await fetch(
                'http://localhost:8000/api/accommodations/',
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(dataToSubmit),
                }
            )

            if (!response.ok) {
                const errorData = await response.json()
                console.error('Error response:', errorData)
                throw new Error('Failed to add accommodation')
            }

            console.log('Accommodation added successfully')
            navigate(`/trips/${tripid}`)
        } catch (error) {
            console.error('Error:', error)
        }
    }

    const handleSubmitAndAddAnother = async (e) => {
        e.preventDefault()

        const dataToSubmit = {
            stays_id: formData.stays_id ? parseInt(formData.stays_id) : null,
            address: formData.address,
            city: formData.city,
            state_province: formData.state_province,
            zip_code: formData.zip_code,
            country: formData.country,
            phone: formData.phone,
            email: formData.email,
            check_in_date: convertToDateTime(formData.check_in_date),
            check_out_date: convertToDateTime(formData.check_out_date),
            number_of_guests: formData.number_of_guests
                ? parseInt(formData.number_of_guests, 10)
                : null,
            total_price: formData.total_price
                ? parseFloat(formData.total_price)
                : null,
            notes: formData.notes || null,
            trip_id: parseInt(tripid, 10),
        }

        try {
            const response = await fetch(
                'http://localhost:8000/api/accommodations/',
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(dataToSubmit),
                }
            )

            if (!response.ok) {
                const errorData = await response.json()
                console.error('Error response:', errorData)
                throw new Error('Failed to add accommodation')
            }

            console.log('Accommodation added successfully')

            setFormData({
                address: '',
                city: '',
                state_province: '',
                zip_code: '',
                country: '',
                phone: '',
                email: '',
                check_in_date: '',
                check_out_date: '',
                number_of_guests: '',
                total_price: '',
                notes: '',
                stays_id: '',
            })
        } catch (error) {
            console.error('Error:', error)
        }
    }

    return (
        <Form className="container w-50 border rounded my-4">
            <h2 className="text-center mt-3">Add Accommodation</h2>
            <Row className="mb-3">
                <Form.Group as={Col} controlId="formStay">
                    <Form.Label>Stay</Form.Label>
                    <Form.Control
                        as="select"
                        name="stays_id"
                        value={formData.stays_id}
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
                        name="state_province"
                        placeholder="Enter state or province"
                        value={formData.state_province}
                        onChange={handleChange}
                    />
                </Form.Group>

                <Form.Group as={Col} controlId="formZipCode">
                    <Form.Label>Zip Code</Form.Label>
                    <Form.Control
                        type="text"
                        name="zip_code"
                        placeholder="Enter zip code"
                        value={formData.zip_code}
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
                        name="number_of_guests"
                        placeholder="Enter number of guests"
                        value={formData.number_of_guests}
                        onChange={handleChange}
                    />
                </Form.Group>
            </Row>

            <Row className="mb-3">
                <Form.Group as={Col} controlId="formCheckInDate">
                    <Form.Label>Check-in Date</Form.Label>
                    <Form.Control
                        type="date"
                        name="check_in_date"
                        value={formData.check_in_date}
                        onChange={handleChange}
                    />
                </Form.Group>

                <Form.Group as={Col} controlId="formCheckOutDate">
                    <Form.Label>Check-out Date</Form.Label>
                    <Form.Control
                        type="date"
                        name="check_out_date"
                        value={formData.check_out_date}
                        onChange={handleChange}
                    />
                </Form.Group>
            </Row>

            <Row className="mb-3">
                <Form.Group as={Col} controlId="formTotalPrice">
                    <Form.Label>Total Price</Form.Label>
                    <Form.Control
                        type="number"
                        name="total_price"
                        placeholder="Enter total price"
                        value={formData.total_price}
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
            <div className="mb-3">
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
            </div>
        </Form>
    )
}

export default AccommodationForm
