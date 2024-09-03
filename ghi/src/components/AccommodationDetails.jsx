 import { NavLink } from "react-router-dom";

 export default function AccommodationDetails({ tripId, accommodations, handleDeleteAccommodation }) {
    const totalPrice = accommodations.reduce((total, accommodation) => total + accommodation.total_price, 0);

    return (
                    <div className="card">
                        <div className="card-body">
                            <h5 className="card-title">Accommodations</h5>
                            {accommodations.length > 0 ? (
                                accommodations.map(accommodation => (
                                    <div key={accommodation.id}>
                                        <p className="card-text">
                                            <span className="font-weight-bold">Address:</span> {accommodation.address}, {accommodation.city}, {accommodation.state_province}, {accommodation.zip_code}, {accommodation.country}
                                        </p>
                                        <p className="card-text">
                                            <span className="font-weight-bold">Phone:</span> {accommodation.phone ? accommodation.phone : 'N/A'}
                                        </p>
                                        <p className="card-text">
                                            <span className="font-weight-bold">Email:</span> {accommodation.email ? accommodation.email : 'N/A'}
                                        </p>
                                        <p className="card-text">
                                            <span className="font-weight-bold">Check-in:</span> {new Date(accommodation.check_in_date).toLocaleDateString()}
                                        </p>
                                        <p className="card-text">
                                            <span className="font-weight-bold">Check-out:</span> {new Date(accommodation.check_out_date).toLocaleDateString()}
                                        </p>
                                        <p className="card-text">
                                            <span className="font-weight-bold">Guests:</span> {accommodation.number_of_guests}
                                        </p>
                                        <p className="card-text">
                                            <span className="font-weight-bold">Total Price:</span> ${accommodation.total_price}
                                        </p>
                                        {accommodation.notes && (
                                            <p className="card-text">
                                                <span className="font-weight-bold">Notes:</span> {accommodation.notes}
                                            </p>
                                        )}
                                        <div className="text-right">
                                            <button
                                                className="btn btn-danger"
                                                onClick={() => handleDeleteAccommodation(accommodation.id)}
                                            >
                                                Delete
                                            </button>
                                        </div>
                                    </div>
                                ))
                            ) : (
                                <p>No accommodation details available.</p>
                            )}
                        </div>
                        <div className="card-footer text-right">
                            <p>Total Price: ${totalPrice}</p>
                            <NavLink to={`/trips/${tripId}/accommodation/`} className="btn btn-success">
                                +
                            </NavLink>
                        </div>
                    </div>
    )
 }
