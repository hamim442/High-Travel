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
    // const [launchInfo, setLaunchInfo] = useState()
    // const [error, setError] = useState(null)

    // useEffect(() => {
    //     async function getData() {
    //         let url = `${API_HOST}/api/launch-details`
    //         console.log('fastapi url: ', url)
    //         let response = await fetch(url)
    //         let data = await response.json()

    //         if (response.ok) {
    //             if (!data.launch_details) {
    //                 console.log('drat! no launch data')
    //                 setError('No launch data')
    //                 return
    //             }
    //             console.log('got launch data!')
    //             setLaunchInfo(data.launch_details)
    //         } else {
    //             console.log('drat! something happened')
    //             setError(data.message)
    //         }
    //     }
    //     getData()
    // }, [])

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
