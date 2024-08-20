import { useState, useEffect } from 'react'
import { Outlet } from 'react-router-dom'
import Nav from './components/Nav'
import ErrorNotification from './components/ErrorNotification'
import './App.css'

// When using environment variables, you should do a check to see if
// they are defined or not and throw an appropriate error message
const API_HOST = import.meta.env.VITE_API_HOST

if (!API_HOST) {
    throw new Error('VITE_API_HOST is not defined')
}

function App() {
    // const [launchInfo, setLaunchInfo] = useState()
    const [error, setError] = useState(null)

    useEffect(() => {
        async function getData() {
            let url = `${API_HOST}/api/launch-details`
            console.log('fastapi url: ', url)
            let response = await fetch(url)
            let data = await response.json()

            if (response.ok) {
                if (!data.launch_details) {
                    console.log('drat! no launch data')
                    setError('No launch data')
                    return
                }
                console.log('got launch data!')
                setLaunchInfo(data.launch_details)
            } else {
                console.log('drat! something happened')
                setError(data.message)
            }
        }
        getData()
    }, [])

    return (
        <div className="App">
            <header className="App-header">
                <Nav />
            </header>
            <Outlet />
            <ErrorNotification error={error} />
        </div>
    )
}

export default App
