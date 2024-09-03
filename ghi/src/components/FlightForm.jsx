import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

export default function FlightForm() {
  const { tripId } = useParams();
  const navigate = useNavigate();

  const [airlines, setAirlines] = useState([]);
  const [formData, setFormData] = useState({
    flight_number: '',
    departure_time: '',
    arrival_time: '',
    departure_airport: '',
    arrival_airport: '',
    price: '',
    airline_id: ''
  });

  useEffect(() => {
    const fetchAirlines = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/airlines');
        if (!response.ok) {
          throw new Error('Failed to fetch airlines');
        }
        const data = await response.json();
        setAirlines(data);
      } catch (error) {
        console.error('Error fetching airlines:', error);
      }
    };

    fetchAirlines();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const dataToSubmit = { ...formData, trip_id: tripId };

    try {
      const response = await fetch('http://localhost:8000/api/flights', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSubmit),
      });

      if (!response.ok) {
        throw new Error('Failed to add flight');
      }

      console.log('Flight added successfully');

      setFormData({
        flight_number: '',
        departure_time: '',
        arrival_time: '',
        departure_airport: '',
        arrival_airport: '',
        price: '',
        airline_id: ''
      });

      navigate(`/trips/${tripId}`);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="container mt-4">
      <div className="mb-3">
        <h2>Add Flight</h2>
      </div>
      <div className="mb-3">
        <label className="form-label">Flight Number:</label>
        <input
          type="text"
          name="flight_number"
          value={formData.flight_number}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Departure Time:</label>
        <input
          type="datetime-local"
          name="departure_time"
          value={formData.departure_time}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Arrival Time:</label>
        <input
          type="datetime-local"
          name="arrival_time"
          value={formData.arrival_time}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Departure Airport:</label>
        <input
          type="text"
          name="departure_airport"
          value={formData.departure_airport}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Arrival Airport:</label>
        <input
          type="text"
          name="arrival_airport"
          value={formData.arrival_airport}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Price:</label>
        <input
          type="number"
          name="price"
          value={formData.price}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Airline:</label>
        <select
          name="airline_id"
          value={formData.airline_id}
          onChange={handleChange}
          className="form-control"
          required
        >
          <option value="" disabled>Select an airline</option>
          {airlines.map((airline) => (
            <option key={airline.id} value={airline.id}>
              {airline.name}
            </option>
          ))}
        </select>
      </div>
      <button type="submit" className="btn btn-primary">Add Flight</button>
    </form>
  );
}
