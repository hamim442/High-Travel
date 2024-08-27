import { NavLink } from 'react-router-dom';

export default function MainTravelPlan() {
    return (
        <div className="container">

            <div className="mt-4">
                <h2>Trip Name</h2>
                <div className="row align-items-center mt-3">
                    <div className="col-md-4">
                        <div className="bg-light border" style={{ height: '150px' }}>
                            {/* Placeholder for image */}
                        </div>
                    </div>
                    <div className="col-md-6">
                        <div className="bg-light p-3">
                            <p>Dates, and other basic info</p>
                            <button className="btn btn-primary">Edit / Delete</button>
                        </div>
                    </div>
                    <div className="col-md-2 text-right">
                        <div>
                            {/* Placeholder for social icons */}
                        </div>
                    </div>
                </div>
            </div>

            <div className="mt-5">
                <div className="row">
                    <div className="col-md-4">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Transportation</h5>
                                <p className="card-text">Details about transportation</p>
                                <button className="btn btn-secondary">Edit / Delete</button>
                            </div>
                            <div className="card-footer text-right">
                                <NavLink to="/transportation" className="btn btn-success">
                                    +
                                </NavLink>
                            </div>
                        </div>
                    </div>

                    <div className="col-md-4">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Accommodation</h5>
                                <p className="card-text">Details about accommodation</p>
                                <button className="btn btn-secondary">Edit / Delete</button>
                            </div>
                            <div className="card-footer text-right">
                                <button className="btn btn-success">+</button>
                            </div>
                        </div>
                    </div>

                    <div className="col-md-4">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">Food/Places/Others</h5>
                                <p className="card-text">Details about food/places/others</p>
                                <button className="btn btn-secondary">Edit / Delete</button>
                            </div>
                            <div className="card-footer text-right">
                                <button className="btn btn-success">+</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
