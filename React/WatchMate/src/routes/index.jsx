import React from 'react'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import HomePage from '../pages/home/home'
import LoginExample from '../pages/Login/login'
import PrivateRoute from './privaterouts'
import StreamPage from '../pages/stream/stream'
const routes = createBrowserRouter([
    {
        path:"/",element: <LoginExample/>
    },
    {
        path:"/home",element:<PrivateRoute><HomePage/></PrivateRoute>,
    },
    {
        path:"/stream",element:<PrivateRoute><StreamPage/></PrivateRoute>,
    }
])
const AppRoutes = () => {
  return (
    <RouterProvider router={routes}/>
  )
}

export default AppRoutes