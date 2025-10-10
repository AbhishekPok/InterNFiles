import React from 'react'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import HomePage from '../pages/home/home'
const routes = createBrowserRouter([
    {
        path:"/",element: <HomePage/>

    },
    // {
    //     path:"/stream",element:<Stream/>,
    // }
])
const AppRoutes = () => {
  return (
    <RouterProvider router={routes}/>
  )
}

export default AppRoutes