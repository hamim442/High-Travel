import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import FlightForm from './FlightForm';
import TrainForm from './TrainForm';
import CarForm from './CarForm';

export default function TransportationPage() {
  const [selectedTransportation, setSelectedTransportation] = useState('');
  const navigate = useNavigate(); // Hook for navigation

  const handleTransportationChange = (e) => {
    setSelectedTransportation(e.target.value);
  };

  const handleBackClick = () => {
    navigate(-1); // Go back to the previous page
  };

  return (
    <div className="container mt-4">
      <button className="btn btn-secondary mb-3" onClick={handleBackClick}>
        Back
      </button>
      <h1>Add Transportation for Trip Name</h1>
      <div className="mb-3">
        <label className="form-label">Select Transportation Type:</label>
        <select
          className="form-select"
          value={selectedTransportation}
          onChange={handleTransportationChange}
        >
          <option value="">Choose...</option>
          <option value="flight">Flight</option>
          <option value="train">Train</option>
          <option value="car">Car</option>
        </select>
      </div>

      {selectedTransportation === 'flight' && <FlightForm />}
      {selectedTransportation === 'train' && <TrainForm />}
      {selectedTransportation === 'car' && <CarForm />}
    </div>
  );
}
