// import { useState, useEffect } from 'react'
import { Outlet } from 'react-router-dom'
import Nav from './components/Nav'
import ErrorNotification from './components/ErrorNotification'
import './App.css'

const API_HOST = import.meta.env.VITE_API_HOST

if (!API_HOST) {
    throw new Error('VITE_API_HOST is not defined')
}

export default function App() {
    return (
        <div className="App">
            <Nav />
            <main className="App-main">
                <Outlet />
            </main>
            <ErrorNotification error={null} /> {/* was previously "error" */}
        </div>
    )
}
