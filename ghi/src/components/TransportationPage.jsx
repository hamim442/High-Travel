import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import FlightForm from './FlightForm';
import TrainForm from './TrainForm';
import CarForm from './CarForm';

export default function TransportationPage() {
  const [selectedTransportation, setSelectedTransportation] = useState('');
  const navigate = useNavigate();

  const handleTransportationChange = (e) => {
    setSelectedTransportation(e.target.value);
  };

  const handleBackClick = () => {
    navigate(-1);
  };

  return (
   <div className="container mt-4">
  <div className="row align-items-center mb-3">
    <div className="col d-flex justify-content-between">
      <h1 className="mb-0">Add Transportation</h1>
      <button className="btn btn-secondary" onClick={handleBackClick}>
        Back
      </button>
    </div>
  </div>
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
