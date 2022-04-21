import React, { Component } from "react";
import { Link, Route } from "react-router-dom";
import UserService from "../services/UserService";
import AlertToast from "./AlertToast";

class LoginComponent extends Component {
  componentDidMount() {
    let localStorage = window.localStorage
    if (localStorage.token) {
      this.props.history.replace('/home');
    }
  }
    
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      password: ""
    };
  }

  userLoginHandler = (e) => {
    
    
    e.preventDefault();
    UserService.login(this.state.username,this.state.password)
      .then((res) => {
        
        window.localStorage.token=res.data.token
        this.props.history.push('/home');
        this.props.history.go();
      })
      .catch((e) => {
        this.setState({ error: e.response.data, errorTimestamp: Date.now() });
      });
  };

  goToRegister = (e) =>{
    this.props.history.push('/register')
  }

  render() {
    return (
      <div>
        <AlertToast
          error={this.state.error}
          errorTimestamp={this.state.errorTimestamp}
        />

        <div className="container">
          <div className="row">
            <div className="card col-md-6 offset-md-3 offset-md-3">
              <h3 className="text-center">Please Login</h3>
              <div className="card-body">
                <form>
                  <div className="form-group">
                    <div className="row mb-3">
                      <label> User Name: </label>
                      <input
                        placeholder="User Name"
                        name="Username"
                        className="form-control"
                        value={this.state.username}
                        onChange={(e) => {
                            this.setState({ username: e.target.value })
                          }}
                      />
                    </div>
                    <div className="row mb-3">
                      <label> Password: </label>
                      <input
                        placeholder="Password"
                        name="Password"
                        className="form-control"
                        type="password"
                        value={this.state.password}
                        onChange={(e) => {
                            this.setState({ password: e.target.value })
                          }}
                      />
                    </div>
                    
                  </div>
                  <div className="row">
                      <Link class="link-primary" to="/register">Sign Up</Link>
                   </div>
                  
                  <button type="submit" class="btn btn-primary" onClick={this.userLoginHandler} >Submit</button>
                  <Link
                    to="/login"
                    className="btn btn-danger"
                    style={{ marginLeft: "10px" }}
                  >
                    Cancel
                  </Link>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default LoginComponent;
