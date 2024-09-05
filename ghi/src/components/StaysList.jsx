import { useState, useEffect } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Spinner from 'react-bootstrap/Spinner'
import Card from 'react-bootstrap/Card'
import Form from 'react-bootstrap/Form'
import AddStayForm from './AddStayForm'

function StaysList() {
    const [stays, setStays] = useState([])
    const [search, setSearch] = useState('')
    const [loading, setLoading] = useState(true)

    const getData = async () => {
        const response = await fetch(
            `${import.meta.env.VITE_API_HOST}/api/stays/`
        )
        if (response.ok) {
            const data = await response.json()
            setTimeout(() => {
                setStays(data)
                setLoading(false)
            }, 1000)
        }
    }

    useEffect(() => {
        getData()
    }, [])

    const addStay = async (newStay) => {
        const response = await fetch(
            `${import.meta.env.VITE_API_HOST}/api/stays/`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(newStay),
            }
        )

        if (response.ok) {
            const addedStay = await response.json()
            setStays((prevStays) => [...prevStays, addedStay])
        }
    }

    return (
        <>
            <AddStayForm onAddStay={addStay} />
            <Container fluid>
                <Row className="justify-content-center mt-5">
                    <Col md={6}>
                        <Form.Group>
                            <Form.Control
                                type="text"
                                value={search}
                                onChange={(e) => setSearch(e.target.value)}
                                placeholder="Search by Keyword"
                                required
                            />
                        </Form.Group>
                    </Col>
                </Row>
            </Container>

            {loading ? (
                <Container
                    className="d-flex justify-content-center align-items-center"
                    style={{ height: '100vh' }}
                >
                    <Spinner animation="border" />
                </Container>
            ) : (
                <Container>
                    <Row className="mt-4">
                        {/* Consider doing this filtering on the server instead using SQL */}
                        {stays
                            .filter((stay) =>
                                search
                                    ? stay.name
                                          .toLowerCase()
                                          .includes(search.toLowerCase())
                                    : true
                            )
                            .map((stay) => (
                                <Col md={4} key={stay.stay_id} className="mb-4">
                                    <Card className="cardHover">
                                        <Card.Img
                                            variant="top"
                                            // Instead of hard coding this URL, consider storing it in a variable,
                                            // or making it optional on the backend with a default database value
                                            src={
                                                stay.logo_picture_url ||
                                                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMAprBWRbfkDNEBHcqH_ZC_nVbr8ViRh6d-g&s'
                                            }
                                            alt={stay.name}
                                            className="cardImage"
                                        />
                                        <Card.Body
                                            className="text-center"
                                            // Try to avoid using inline styles and put this in CSS
                                            style={{
                                                backgroundColor: '#B7BFAA',
                                            }}
                                        >
                                            <Card.Title
                                                style={{ color: '#5A735B' }}
                                            >
                                                {stay.name}
                                            </Card.Title>
                                        </Card.Body>
                                    </Card>
                                </Col>
                            ))}
                    </Row>
                </Container>
            )}
        </>
    )
}

export default StaysList
