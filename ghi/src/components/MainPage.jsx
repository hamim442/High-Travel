import { NavLink } from 'react-router-dom'

function MainPage() {
    return (
        <div className="px-4 py-5 my-5 text-center">
            <h1 className="display-5 fw-bold">High Travel</h1>
            <div className="col-lg-6 mx-auto">
                <p className="lead mb-4">
                    Experience the high of planning your trips with us.
                </p>
                <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
                    <NavLink
                        to="/signin"
                        className="btn btn-primary btn-lg px-4 me-sm-3"
                    >
                        Sign In
                    </NavLink>
                    <NavLink
                        to="/signup"
                        className="btn btn-outline-secondary btn-lg px-4"
                    >
                        Sign Up
                    </NavLink>
                </div>
                <div className="d-grid gap-2 d-sm-flex justify-content-sm-center mt-4">
                    <NavLink
                        to="/create-plan"
                        className="btn btn-success btn-lg px-4"
                    >
                        Create a Plan
                    </NavLink>
                    <NavLink
                        to="/your-plans"
                        className="btn btn-info btn-lg px-4"
                    >
                        Your Most Recent Plans
                    </NavLink>
                    <NavLink
                        to="/popular-destinations"
                        className="btn btn-warning btn-lg px-4"
                    >
                        Popular Destinations
                    </NavLink>
                </div>
            </div>
        </div>
    )
}

export default MainPage
