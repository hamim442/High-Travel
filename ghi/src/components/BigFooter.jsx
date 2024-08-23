import './styles/Footer.css'

export default function BigFooter() {
    return (
        <footer className="bigfoot text-center text-lg-start bg-body-tertiary text-muted">
            {/* Section: Links */}
            <section>
                <div className="container text-center text-md-start mt-5">
                    <div className="row mt-3">
                        {/* Company info */}
                        <div className="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
                            <h6 className="text-uppercase fw-bold mb-4">
                                <i className="fas fa-gem me-3"></i>HighTravel
                            </h6>
                            <p>
                                High Travel is your all-in-one companion for
                                seamless adventure planning, helping you
                                organize every aspect of your journey with ease.
                                From crafting detailed itineraries to
                                discovering hidden gems, we are here to elevate
                                your travel experience and turn your wanderlust
                                into unforgettable memories.
                            </p>
                        </div>

                        {/* Partners */}
                        <div className="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
                            <h6 className="text-uppercase fw-bold mb-4">
                                Partners
                            </h6>
                            <p>
                                <a href="#!" className="text-reset">
                                    Google
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-reset">
                                    TripAdvisor
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-reset">
                                    OpenAI
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-reset">
                                    Hack Reactor
                                </a>
                            </p>
                        </div>

                        {/* Other Links */}
                        <div className="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
                            <h6 className="text-uppercase fw-bold mb-4">
                                Other Links
                            </h6>
                            <p>
                                <a href="#!" className="text-reset">
                                    History
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-reset">
                                    Team
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-reset">
                                    Careers
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-reset">
                                    Help
                                </a>
                            </p>
                        </div>

                        {/* Contact */}
                        <div className="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
                            <h6 className="text-uppercase fw-bold mb-4">
                                Contact
                            </h6>
                            <p>
                                <i className="fas fa-home me-3"></i> New York,
                                NY 10012, US
                            </p>
                            <p>
                                <i className="fas fa-envelope me-3"></i>{' '}
                                info@example.com
                            </p>
                            <p>
                                <i className="fas fa-phone me-3"></i> + 01 234
                                567 88
                            </p>
                            <p>
                                <i className="fas fa-print me-3"></i> + 01 234
                                567 89
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            {/* Copyright */}
            <div
                className="text-center p-4"
                style={{ backgroundColor: 'rgba(0, 0, 0, 0.05)' }}
            >
                © 2024 Copyright:{' '}
                <a className="text-reset fw-bold" href="#!">
                    HighTravel.com
                </a>
            </div>
        </footer>
    )
}
