import { useState } from 'react'
import { Form, Button, Container, Row, Col } from 'react-bootstrap'

function AddStayForm({ onAddStay }) {
    const [name, setName] = useState('')
    const [logoPictureUrl, setLogoPictureUrl] = useState('')

    const handleSubmit = async (e) => {
        e.preventDefault()

        const newStay = {
            name,
            logo_picture_url: logoPictureUrl,
        }

        onAddStay(newStay)
        setName('')
        setLogoPictureUrl('')
    }

    return (
        <Container>
            <Row className="justify-content-center mt-5">
                <Col md={6}>
                    <h2>Add a New Stay</h2>
                    <Form onSubmit={handleSubmit}>
                        <Form.Group controlId="name" className="mb-3">
                            <Form.Label>Stay Name</Form.Label>
                            <Form.Control
                                type="text"
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                                placeholder="Enter stay name"
                                required
                            />
                        </Form.Group>

                        <Form.Group controlId="logoPictureUrl" className="mb-3">
                            <Form.Label>Logo Picture URL</Form.Label>
                            <Form.Control
                                type="text"
                                value={logoPictureUrl}
                                onChange={(e) =>
                                    setLogoPictureUrl(e.target.value)
                                }
                                placeholder="Enter logo picture URL"
                            />
                        </Form.Group>

                        <Button variant="primary" type="submit">
                            Add Stay
                        </Button>
                    </Form>
                </Col>
            </Row>
        </Container>
    )
}

export default AddStayForm
