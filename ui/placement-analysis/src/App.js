import React, { Component } from 'react';
import './App.css';
import Form from 'react-bootstrap/Form';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.css';

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      formData: {
        select1: 0,
        select2: 0,
        select3: 0,
        select4: 0,
        select5: 0,
        select6: 0,
        select7: 0,
        select8: 0,
        select9: 0,
        select10:0,
        select11: 0,
        select12: 0
      },
      result: ""
    };
  }

  handleChange = (event) => {
    const value = event.target.value;
    const name = event.target.name;
    var formData = this.state.formData;
    formData[name] = value;
    this.setState({
      formData
    });
  }

  handlePredictClick = (event) => {
    const formData = this.state.formData;
    this.setState({ isLoading: true });
    fetch('http://127.0.0.1:5000/predict', 
      {
        method: 'POST',       
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }, 
        body: JSON.stringify(formData)
      })
      .then(response => response.json())
      .then(response => {
        console.log(response)
        this.setState({
          result: response.result,
          isLoading: false
        });
      });
  }

  handleCancelClick = (event) => {
    this.setState({ result: "" });
  }

  render() {
    const isLoading = this.state.isLoading;
    const formData = this.state.formData;
    const result = this.state.result;

    return (
      <Container-fluid>
        <div>
          <h1 className="title">Placement prediction</h1>
        </div>
        <div className="content">
          <Form>
            <Form.Row>
            <Form.Group as={Col}>
                <Form.Label>MBA percentage</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select12}
                  name="select12"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>less than 51%</option>
                  <option>51% to 57%</option>
                  <option>57% to 62%</option>
                  <option>62% to 66%</option>
                  <option>66% to 77%</option>
                  <option>77% to 100%</option>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>10th percentage</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select2}
                  name="select2"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>less than 40%</option>
                  <option>40% to 60%</option>
                  <option>60% to 67%</option>
                  <option>67% to 75%</option>
                  <option>75% to 90%</option>
                  <option>90% to 100%</option>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>UG-Degree percentage</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select7}
                  name="select7"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>less than 50%</option>
                  <option>50% to 61%</option>
                  <option>61% to 66%</option>
                  <option>66% to 72%</option>
                  <option>72% to 80%</option>
                  <option>80% to 91%</option>
                  <option>greater than 91%</option>
                </Form.Control>
              </Form.Group>
            </Form.Row>
            <Form.Row>
              <Form.Group as={Col}>
                <Form.Label>12th Stream</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select6}
                  name="select6"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>Science</option>
                  <option>Commerce</option>
                  <option>Arts</option>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>12th Board</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select5}
                  name="select5"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>CBSE</option>
                  <option>Other boards</option>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>12th percentage</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select4}
                  name="select4"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>less than 37%</option>
                  <option>37% to 50%</option>
                  <option>50% to 60%</option>
                  <option>60% to 65%</option>
                  <option>65% to 73%</option>
                  <option>73% to 83%</option>
                  <option>83% to 90%</option>
                  <option>greater than 90%</option>
                </Form.Control>
              </Form.Group>
            </Form.Row>
            <Form.Row>
            <Form.Group as={Col}>
                <Form.Label>Gender</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select1}
                  name="select1"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>Male</option>
                  <option>Female</option>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Field of Degree</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select8}
                  name="select8"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>Science and Tech</option>
                  <option>Commerce and Management</option>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Work Experience</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select9}
                  name="select9"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>Yes</option>
                  <option>No</option>
                </Form.Control>
              </Form.Group>
            </Form.Row>
            <Form.Row>
            <Form.Group as={Col}>
                <Form.Label>10th Board</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select3}
                  name="select3"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>CBSE</option>
                  <option>Other boards</option>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Employement-test percentage</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select10}
                  name="select10"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>less than 50%</option>
                  <option>50% to 60%</option>
                  <option>60% to 71%</option>
                  <option>71% to 83%</option>
                  <option>83% to 90%</option>
                  <option>greater than 90%</option>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>MBA specialization</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.select11}
                  name="select11"
                  onChange={this.handleChange}>
                  <option>Select</option>
                  <option>Marketing and HR</option>
                  <option>Marketing and Finance</option>
                </Form.Control>
              </Form.Group>
            </Form.Row>
            <Row>
              <Col>
                <Button
                  block
                  variant="success"
                  disabled={isLoading}
                  onClick={!isLoading ? this.handlePredictClick : null}>
                  { isLoading ? 'Making prediction' : 'Predict' }
                </Button>
              </Col>
              <Col>
                <Button
                  block
                  variant="danger"
                  disabled={isLoading}
                  onClick={this.handleCancelClick}>
                  Reset prediction
                </Button>
              </Col>
            </Row>
          </Form>
          {result === "" ? null :
            (<Row>
              <Col className="result-container">
                <h5 id="result">{result}</h5>
              </Col>
            </Row>)
          }
        </div>
      </Container-fluid>
    );
  }
}

export default App;
