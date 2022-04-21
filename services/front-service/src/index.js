import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route, Redirect } from "react-router-dom";
import App from "./App";
import Login from "./components/LoginComponent"
import Register from "./components/RegisterComponent"

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
        <Route path="/login" component={Login}/>
        <Route path="/home" component={App}/>
        <Route path='/register' component={Register}></Route>
        <Redirect path="/" to="/login" exact />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);
