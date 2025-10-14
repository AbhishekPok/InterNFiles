// import { useState } from 'react';
import { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Modal from 'react-bootstrap/Modal';
import {createMovies, updateMovie, deleteMovie}  from '../../services/movie';


function MovieModal(props) {
  const {show, handleClose,setRefesh,selectedMovie} = props;
  const[FormData, setFormData] = useState({title:"",storyline:"",active:false,created_at:""})

  const handleChange = (e) =>{
    const {name, value} = e.target
    setFormData((prev) => {
    const updateFormData = { ...prev, [name]:value};
    return updateFormData
    });
  };
  
console.log("selected movee", selectedMovie);


  const handleSumbit = async() => {
    // console.log("k hudai xa yeha")
    if (selectedMovie){
      await updateMovie(selectedMovie.id, FormData);
    }
    else{
    await createMovies(FormData);
    }
    handleClose();
    setRefesh((prev) => !prev);
  };
  useEffect(() => {
    if (selectedMovie){
      setFormData({
        title:selectedMovie.title,
        storyline:selectedMovie.storyline,
        active:selectedMovie.active,
      })
    }
    else {
      setFormData({title:"",storyline:"",active:false,})
    }
  },[selectedMovie])


  return (
    <>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Enter Details</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
              <Form.Label>Name of the Movie</Form.Label>
              <Form.Control
                name="title"
                type="text"
                placeholder="Movie Name"
                onChange={handleChange}
                defaultValue={selectedMovie?.title?? ""}
                autoFocus
              />
            </Form.Group>
            <Form.Group
              className="mb-3"
              controlId="exampleForm.ControlTextarea1"
            >
              <Form.Label>StoryLine</Form.Label>
              <Form.Control 
              name="storyline"
              as="textarea" 
              onChange={handleChange}
              defaultValue={selectedMovie?.storyline?? ""}
              rows={3} 
              />
              <Form.Label>Is Active</Form.Label>
              <Form.Check 
              type="radio" 
              name="active" 
              label="Active" 
              onChange={handleChange}
              defaultChecked={selectedMovie?.active ?? ""}
              />
              <Form.Check 
              type="radio" 
              name="active" 
              label="In-active " 
              onChange={handleChange}
              defaultChecked={selectedMovie?.active ?? ""}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary" onClick={handleSumbit}>
            {
              selectedMovie?.title ? "Update Movie" : "Create Movie"
            }
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}
export default MovieModal;