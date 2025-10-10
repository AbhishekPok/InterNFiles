import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import myImg from "../../img/dashboard.png"

function NewNavbar() {
  return (
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
        <Nav className="justify-content-end">
        <Container>
                <Navbar.Brand href="#home">
                  <img
                  src={myImg}
                  width="30"
                  height="30"
                  className="float-left align-top"
                  alt="dashbord"
                  />
                </Navbar.Brand>
        </Container>
        </Nav>
        <Navbar.Brand>Todo List</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Navbar className="bg-body-tertiary">
              <Nav.Link href="#home">Home</Nav.Link>
              <Nav.Link href="#progress">Progress</Nav.Link>
              <NavDropdown title="More" id="basic-nav-dropdown">
                <NavDropdown.Item href="#notes">Notes</NavDropdown.Item>
                <NavDropdown.Item href="#history">History</NavDropdown.Item>
                <NavDropdown.Item href="#aboutme">About Me</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#watchMate">
                 WatchMate Project
                </NavDropdown.Item>
              </NavDropdown>
            </Navbar>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NewNavbar;