import { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

export default function CarForm() {
  const { tripId } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    car_model: '',
    rental_company: '',
    pickup_time: '',
    dropoff_time: '',
    pickup_location: '',
    dropoff_location: '',
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
      const response = await fetch('http://localhost:8000/api/cars', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSubmit),
      });

      if (!response.ok) {
        throw new Error('Failed to add car');
      }

      console.log('Car added successfully');
      setFormData({
        car_model: '',
        rental_company: '',
        pickup_time: '',
        dropoff_time: '',
        pickup_location: '',
        dropoff_location: '',
        price: ''
      });

      navigate(`/trips/${tripId}`);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="container mt-4">
      <div className="mb-3">
        <h2>Add Car</h2>
      </div>
      <div className="mb-3">
        <label className="form-label">Car Model:</label>
        <input
          type="text"
          name="car_model"
          value={formData.car_model}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Rental Company:</label>
        <input
          type="text"
          name="rental_company"
          value={formData.rental_company}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Pickup Time:</label>
        <input
          type="datetime-local"
          name="pickup_time"
          value={formData.pickup_time}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Dropoff Time:</label>
        <input
          type="datetime-local"
          name="dropoff_time"
          value={formData.dropoff_time}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Pickup Location:</label>
        <input
          type="text"
          name="pickup_location"
          value={formData.pickup_location}
          onChange={handleChange}
          className="form-control"
          required
        />
      </div>
      <div className="mb-3">
        <label className="form-label">Dropoff Location:</label>
        <input
          type="text"
          name="dropoff_location"
          value={formData.dropoff_location}
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
      <button type="submit" className="btn btn-primary">Add Car</button>
    </form>
  );
}
