import React, { Component } from "react";
import { Link } from "react-router-dom";
import UrlShortenerService from "../services/UrlShortenerService";
import AlertToast from "./AlertToast";

class CreateUrlShortenerComponent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      id: this.props.match.params.id,
      url: "",
      error: "",
      errorTimestamp: -1,
    };
    this.changeUrlAddressHandler = this.changeUrlAddressHandler.bind(this);
    this.saveUrlShortener = this.saveUrlShortener.bind(this);
  }

  saveUrlShortener = (e) => {
    e.preventDefault();
    UrlShortenerService.createUrlShortener(this.state.url)
      .then(() => {
        this.props.history.push("/url-shortener-list");
      })
      .catch((e) => {
        this.setState({ error: e.response.data, errorTimestamp: Date.now() });
      });
  };

  changeUrlAddressHandler = (event) => {
    this.setState({ url: event.target.value });
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
              <h3 className="text-center">Add Url Shortener</h3>
              <div className="card-body">
                <form>
                  <div className="form-group">
                    <label> Url Address: </label>
                    <input
                      placeholder="Url Address"
                      name="url"
                      className="form-control"
                      value={this.state.url}
                      onChange={this.changeUrlAddressHandler}
                    />
                  </div>
                  <button
                    className="btn btn-success"
                    onClick={this.saveUrlShortener}
                  >
                    Save
                  </button>
                  <Link
                    to="/url-shortener-list"
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

export default CreateUrlShortenerComponent;
