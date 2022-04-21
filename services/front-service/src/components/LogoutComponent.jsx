import { Component } from "react";

class LogoutComponent extends Component {
  
  componentDidMount() {
    let localStorage = window.localStorage
    if(localStorage.loginToken){
        localStorage.loginToken = ""
    }
    this.props.history.push('/login')
  }
  render() {
    return null;
  }
}

export default LogoutComponent;
