// import { useState } from 'react';
import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Modal from 'react-bootstrap/Modal';
import { createMovies } from '../../services/movie';


function MovieModal(props) {
  const {show, handleShow, handleClose,setRefesh} = props;
  const[FormData, setFormData] = useState({title:"",storyline:"",active:"",created_at:""})

  const handleChange = (e) =>{
    const {name, value} = e.target
    setFormData((prev) => {
    const updateFormData = { ...prev, [name]:value};
    return updateFormData
    });
  };
  
  const handleSumbit = async() => {
    // console.log("k hudai xa yeha")
    await createMovies(FormData);
    handleClose();
    setRefesh((prev) => !prev);
  };
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
              rows={3} 
              />
              <Form.Label>Is Active</Form.Label>
              <Form.Check type="radio" name="active" label="Active" onChange={handleChange}/>
              <Form.Check type="radio" name="active" label="In-active " onChange={handleChange}/>
              <Form.Label>Created At</Form.Label>
              <Form.Control
                name="created_at"
                type="date"
                placeholder="Enter a Date"
                onChange={handleChange}
                autoFocus
              />

            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary" onClick={handleSumbit}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default MovieModal;