import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import myImg from "../../img/dashboard.png"
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import Input from 'react-bootstrap/FormControl'
import './navbar.css'
function NewNavbar() {
  return (
    <Navbar expand="xxl" className="bg-body-tertiary navbar mb-3">
      <Container>
        <Nav className="justify-content-end">
          <Container>
            <Navbar.Brand href="#home">
                <img
                  src={myImg}
                  width="30"
                  height="30"
                  className="float-left align-top"
                  alt="dashboard"
                  />
            </Navbar.Brand>
          </Container>
        </Nav>
        <Navbar.Brand>Todo List</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav"/>
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Navbar className="bg-body-tertiary">
              <Nav.Link href="#home">Home</Nav.Link>
              <Nav.Link href="#progress">Progress</Nav.Link>
              <NavDropdown title="More" id="basic-nav-dropdown">
                <NavDropdown.Item href="#notes">Notes</NavDropdown.Item>
                <NavDropdown.Item href="#history">History</NavDropdown.Item>
                <NavDropdown.Item href="#aboutme">About Me</NavDropdown.Item>
                <NavDropdown.Item href="#watchMate">WatchMate Project</NavDropdown.Item>
              </NavDropdown>
              <Container>
              <Form className = "d-flex"role="search">
              <Input className="form-control me-2"  type="search" placeholder="Search" aria-label="Search"/>
              <Button className="btn btn-outline-success" type = "submit" variant="outline-success">Search</Button>
              </Form>
              </Container>
            </Navbar>
          </Nav>
        </Navbar.Collapse>
        </Container>
      </Navbar>
  );
}



export default NewNavbar;