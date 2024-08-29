import App from './App'
import React from 'react'
import ReactDOM from 'react-dom/client'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import AuthProvider from './components/AuthProvider'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'

import SignInForm from './components/SignInForm'
import SignUpForm from './components/SignUpForm'
import MainPage from './components/MainPage'
import CityPage from './components/CityPage'
import UserTravelPlans from './components/UsersTravelPlan'
import TransportationPage from './components/TransportationPage'
import MainTravelPlan from './components/MainTravelPlan'
import CreateTravelPlan from './components/CreateTravelPlan'
import StaysList from './components/StaysList'
import AddStayForm from './components/AddStayForm'
import ProfilePage from './components/ProfilePage'
import EditUserProfile from './components/EditUserProfile'
import CreateNewCity from './components/CreateNewCity'
import AccommodationForm from './components/Accommodations'

const BASE_URL = import.meta.env.BASE_URL
if (!BASE_URL) {
    throw new Error('BASE_URL is not defined')
}

const router = createBrowserRouter(
    [
        {
            path: '/',
            element: <App />,
            children: [
                {
                    path: '/',
                    element: <MainPage />,
                },
                {
                    path: 'signup',
                    element: <SignUpForm />,
                },
                {
                    path: 'signin',
                    element: <SignInForm />,
                },
                {
                    path: 'city/:cityId',
                    element: <CityPage />,
                },
                {
                    path: 'stays',
                    element: <StaysList />,
                },
                {
                    path: 'stays',
                    element: <AddStayForm />,
                },
                {
                    path: 'trips/:tripId/transportation',
                    element: <TransportationPage />,
                },
                {
                    path: 'trips/:tripId',
                    element: <MainTravelPlan />,
                },

                {
                    path: 'create',
                    element: <CreateTravelPlan />,
                },
                {
                    path: 'accommodations',
                    element: <AccommodationForm />,
                },
                {
                    path: 'profile',
                    element: <ProfilePage />,
                },
            ],
        },
    ],
    {
        basename: BASE_URL,
    }
)

const rootElement = document.getElementById('root')
if (!rootElement) {
    throw new Error('root element was not found!')
}

const root = ReactDOM.createRoot(rootElement)
root.render(
    <React.StrictMode>
        <AuthProvider>
            <RouterProvider router={router} />
        </AuthProvider>
    </React.StrictMode>
)
