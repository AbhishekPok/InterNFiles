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
import { deleteMovie } from '../../services/movie.js';

function StreamPage() {
  const [selectedMovie, setselectedMovie] = useState(null);
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

  const onEdit = (movie) =>{
      console.log("edit call bhairako xa.")
      handleShow();
      setselectedMovie(movie);
  }

  const onDelete = (movieId) =>{
      deleteMovie(movieId)
    }
  
return (
    <>
    <NavbarComponent/>
      <Button variant="primary" onClick={handleShow} style={{float:"right"}}>
        Create Movie
      </Button>
      <TableComponent movies = {moviesList} onEdit = {onEdit} onDelete = {onDelete}/>
      <MovieModal 
      show={show} 
      selectedMovie ={selectedMovie} 
      setRefesh={setRefesh} 
      handleClose={handleClose}
      />
    </>
  )
}

export default StreamPage
