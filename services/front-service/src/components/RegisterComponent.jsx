import React, { Component } from "react";
import { Link } from "react-router-dom";
import UserService from "../services/UserService";
import AlertToast from "./AlertToast";

class RegisterComponent extends Component {
  componentDidMount() {
    let localStorage = window.localStorage
    if (localStorage.loginToken) {
      this.props.history.replace('/home')
    }
  }
    
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      password: "",
      pwdConfirm: ""
    };
  }

  userRegisterHandler = (e) => {
    
    
    e.preventDefault();
    UserService.createUser(this.state.username,this.state.password)
      .then(() => {
        this.props.history.replace('/')
      })
      .catch((e) => {
        this.setState({ error: e.response.data, errorTimestamp: Date.now() });
      });
  };

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
              <h3 className="text-center">Sign Up</h3>
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
                  <button type="submit" class="btn btn-primary" onClick={this.userRegisterHandler} >Submit</button>
                  <Link
                    to="/"
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

export default RegisterComponent;
