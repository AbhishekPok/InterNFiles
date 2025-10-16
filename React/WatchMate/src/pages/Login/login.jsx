import Form from "react-bootstrap/Form";
import { Container, Row, Col, Button } from "react-bootstrap";
import { useState } from "react";
import { login } from "../../services/form";
import { useNavigate } from "react-router-dom";

function LoginExample() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });
  const [error, setError] = useState("");
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    const tokenData = await login(formData);
    if (tokenData.non_field_errors) {
      console.log("data:", tokenData);
      window.alert(`${tokenData?.non_field_errors[0]}`);
    } else {
      if (tokenData.token) {
        localStorage.setItem("authToken", tokenData?.token);
        navigate("/home");
      }
    }
    // console.log("tokenData", tokenData)
    // window.alert("Login Successful")
    console.log("formData", formData);
  };
  return (
    <Container className="mt-5">
      <Row className="justify-content-md-center">
        <Col md={4}>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3" controlId="formGroupEmail">
              <Form.Label>UserName</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter Username"
                name="username"
                onChange={handleChange}
              />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formGroupPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Password"
                name="password"
                onChange={handleChange}
              />
            </Form.Group>
            <Button variant="primary" type="submit" className="w-100" onClick = {handleSubmit}>
              Login
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
}
export default LoginExample;
