// import { useEffect, useState } from 'react'
// import NavbarComponent from '../components/NavBar/NavBar.jsx'
// import TableComponent from "../components/table/table.jsx"
// import { listMovie } from '../services/movie.js'
// import MovieModal from '../components/MovieModals/movieModals.jsx'
import Button from 'react-bootstrap/esm/Button'

import { useEffect, useState } from "react";
import {listMovie} from "../../services/movie";
import TableComponent from '../../components/table/table';
import MovieModal from '../../components/MovieModals/movieModals';
import NavbarComponent from '../../components/NavBar/NavBar';

function HomePage() {
  const [moviesList, setMoviesList] = useState([]);
  const [show, setShow] = useState(false);
  const [refresh, setRefesh] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);


  useEffect(() => {
    const movies = listMovie();
    movies.then((data) => {
      setMoviesList(data);
    })
    .catch((error) =>{
      console.log(error)
    })
  },[refresh])

  
return (
    <>
    <NavbarComponent/>
      <Button variant="primary" onClick={handleShow} style={{float:"right"}}>
        Create Movie
      </Button>
      <TableComponent movies = {moviesList}/>
      <MovieModal show={show} handleShow={handleShow} setRefesh={setRefesh} handleClose={handleClose}/>
    </>
  )
}

export default HomePage
