import { Component } from "react";

class CheckLoginComponent extends Component {
    
  componentDidMount() {
    let localStorage = window.localStorage
    if(localStorage.loginToken){

    }else{
        this.props.history.push("/login")
    }
  }
  render() {
    return null;
  }
}

export default CheckLoginComponent;
