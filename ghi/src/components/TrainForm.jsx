import { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

export default function TrainForm() {
  const { tripId } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    train_number: '',
    departure_time: '',
    arrival_time: '',
    departure_station: '',
    arrival_station: '',
    price: ''
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

    const dataToSubmit = { ...formData, trip_id: tripId };

    try {
      const response = await fetch('http://localhost:8000/api/trains', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSubmit),
      });

      if (!response.ok) {
        throw new Error('Failed to add train');
      }

      console.log('Train added successfully');
      setFormData({
        train_number: '',
        departure_time: '',
        arrival_time: '',
        departure_station: '',
        arrival_station: '',
        price: ''
      });

      navigate(`/trips/${tripId}`);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="container mt-4 border rounded w-50 mb-3 p-4">
      <div className="mb-3">
        <h2 className="text-center py-3">Add Train Ride</h2>
      </div>
      <div className="mb-3">
        <label className="form-label">Train Number:</label>
        <input
          type="text"
          name="train_number"
          value={formData.train_number}
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
        <label className="form-label">Departure Station:</label>
        <input
          type="text"
          name="departure_station"
          value={formData.departure_station}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Arrival Station:</label>
        <input
          type="text"
          name="arrival_station"
          value={formData.arrival_station}
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
      <button type="submit" className="btn btn-primary">Add Train</button>
    </form>
  );
}
