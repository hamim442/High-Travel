import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

export default function EditTrain() {
  const { trainId, tripId } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    train_number: '',
    departure_time: '',
    arrival_time: '',
    departure_station: '',
    arrival_station: '',
    price: ''
  });

  useEffect(() => {
    const fetchTrain = async () => {
      try {
        const response = await fetch(`http://localhost:8000/api/trains/${trainId}`);
        if (!response.ok) {
          throw new Error('Failed to fetch train');
        }
        const train = await response.json();
        setFormData({
          train_number: train.train_number,
          departure_time: new Date(train.departure_time).toISOString().slice(0, -1),
          arrival_time: new Date(train.arrival_time).toISOString().slice(0, -1),
          departure_station: train.departure_station,
          arrival_station: train.arrival_station,
          price: train.price
        });
      } catch (error) {
        console.error('Error fetching train details:', error);
      }
    };

    fetchTrain();
  }, [trainId]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
  e.preventDefault();

  const dataToSubmit = {
    ...formData,
    trip_id: tripId,
    train_id: trainId
  };

  console.log('Data to submit:', dataToSubmit);

  try {
    const response = await fetch(`http://localhost:8000/api/trains/${trainId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dataToSubmit),
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error('Error data:', errorData);
      throw new Error(`Failed to update train: ${errorData.message || response.statusText}`);
    }

    console.log('Train updated successfully');
    navigate(-1);
  } catch (error) {
    console.error('Error:', error);
  }
};

  return (
    <form onSubmit={handleSubmit} className="container mt-4">
      <div className="mb-3">
        <h2>Edit Train Ride</h2>
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
      <button type="submit" className="btn btn-primary">Update Train</button>
    </form>
  );
}
