import React, { Component } from "react";
import { Link } from "react-router-dom";
import UrlShortenerService from "../services/UrlShortenerService";
import AlertToast from "./AlertToast";

class UpdateUrlShortenerComponent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      id: this.props.match.params.id,
      urlAddress: "",
      error: "",
      errorTimestamp: -1,
    };
    this.changeUrlAddressHandler = this.changeUrlAddressHandler.bind(this);
    this.updateUrlShortener = this.updateUrlShortener.bind(this);
  }

  updateUrlShortener = (e) => {
    e.preventDefault();
    UrlShortenerService.updateUrlShortener(this.state.urlAddress, this.state.id)
      .then(() => {
        this.props.history.push("/home/url-shortener-list");
      })
      .catch((e) => {
        this.setState({ error: e.response.data, errorTimestamp: Date.now() });
      });
  };

  changeUrlAddressHandler = (event) => {
    this.setState({ urlAddress: event.target.value });
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
              <h3 className="text-center">Update Url Shortener</h3>
              <div className="card-body">
                <form>
                  <div className="form-group">
                    <label>New Url Address: </label>
                    <input
                      placeholder="Url Address"
                      name="urlAddress"
                      className="form-control"
                      value={this.state.urlAddress}
                      onChange={this.changeUrlAddressHandler}
                    />
                  </div>

                  <button
                    className="btn btn-success"
                    onClick={this.updateUrlShortener}
                  >
                    Save
                  </button>
                  <Link
                    to="/home/url-shortener-list"
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

export default UpdateUrlShortenerComponent;
