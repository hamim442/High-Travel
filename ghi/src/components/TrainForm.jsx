import { useState } from 'react';

export default function TrainForm() {
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

    try {
      const response = await fetch('http://localhost:8000/api/trains', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
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
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="container mt-4">
      <div className="mb-3">
        <h2>Add Train Ride</h2>
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
