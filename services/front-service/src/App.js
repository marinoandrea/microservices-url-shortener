import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import CreateUrlShortenerComponent from "./components/CreateUrlShortenerComponent";
import FooterComponent from "./components/FooterComponent";
import HeaderComponent from "./components/HeaderComponent";
import ListUrlShortenerComponent from "./components/ListUrlShortenerComponent";
import UpdateUrlShortenerComponent from "./components/UpdateUrlShortenerComponent";
import CheckLoginComponent from "./components/CheckLoginComponent"
function App() {
  return (
    <div>
      <Router>
        <HeaderComponent />
        <div className="container" style={{ padding: 20 }}>
          <Switch>
            <Route path="/home" exact component={ListUrlShortenerComponent}></Route>
            <Route
              path="/home/url-shortener-list"
              component={ListUrlShortenerComponent}
            ></Route>
            <Route
              path="/home/add-url-shortener"
              component={CreateUrlShortenerComponent}
            ></Route>
            <Route
              path="/home/update-url-shortener/:id"
              component={UpdateUrlShortenerComponent}
            ></Route>
          </Switch>
        </div>
        <FooterComponent />
      </Router>
    </div>
  );
}

export default App;
