import { useState } from 'react';

function FlightForm() {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    departure_time: '',
    arrival_time: '',
    departure_airport: '',
    arrival_airport: '',
    flight_number: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('/api/flights', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Failed to add flight');
      }

      console.log('Flight added successfully');
      setFormData({
        name: '',
        description: '',
        departure_time: '',
        arrival_time: '',
        departure_airport: '',
        arrival_airport: '',
        flight_number: ''
      });
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Name:</label>
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Description:</label>
        <input
          type="text"
          name="description"
          value={formData.description}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Departure Time:</label>
        <input
          type="datetime-local"
          name="departure_time"
          value={formData.departure_time}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Arrival Time:</label>
        <input
          type="datetime-local"
          name="arrival_time"
          value={formData.arrival_time}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Departure Airport:</label>
        <input
          type="text"
          name="departure_airport"
          value={formData.departure_airport}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Arrival Airport:</label>
        <input
          type="text"
          name="arrival_airport"
          value={formData.arrival_airport}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Flight Number:</label>
        <input
          type="number"
          name="flight_number"
          value={formData.flight_number}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit">Add Flight</button>
    </form>
  );
}

export default FlightForm;
