import React, { Component } from "react";
import UrlShortenerService, { ROUTE } from "../services/UrlShortenerService";

class ListUrlShortenerComponent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      urlShorteners: [],
      error: "",
      errorTimestamp: -1,
    };
    this.addUrlShortener = this.addUrlShortener.bind(this);
    this.editUrlShortener = this.editUrlShortener.bind(this);
    this.deleteUrlShortener = this.deleteUrlShortener.bind(this);
  }

  deleteUrlShortener(id) {
    UrlShortenerService.deleteUrlShortenerById(id).then((res) => {
      this.setState({
        urlShorteners: this.state.urlShorteners.filter(
          (urlShortener) => urlShortener !== id
        ),
      });
    });
  }

  editUrlShortener(id) {
    this.props.history.push(`/home/update-url-shortener/${id}`);
  }

  componentDidMount() {
    UrlShortenerService.getUrlShortener().then((res) => {
      console.log(res);
      if (res.data) {
        this.setState({
          urlShorteners: res.data,
        });
      }
    });
  }

  addUrlShortener() {
    this.props.history.push("/home/add-url-shortener");
  }

  render() {
    return (
      <div>
        <h2 className="text-center">Url Shortener List</h2>
        <div className="row">
          <button className="btn btn-primary" onClick={this.addUrlShortener}>
            Add UrlShortener
          </button>
        </div>
        <br></br>
        <div className="row">
          <table className="table table-striped table-bordered">
            <thead>
              <tr>
                <th>Url Shortener Id</th>
                <th>Shortened URL</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {this.state.urlShorteners.map((urlShortener) => (
                <tr key={urlShortener}>
                  <td>{urlShortener}</td>
                  <td>
                    <a
                      href={`${ROUTE}/${urlShortener}`}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      {`${window.location.host}${ROUTE}/${urlShortener}`}
                    </a>
                  </td>
                  {/*<td>{urlShortener.original_address}</td>*/}
                  <td>
                    <button
                      onClick={() => this.editUrlShortener(urlShortener)}
                      className="btn btn-info"
                    >
                      Update
                    </button>
                    <button
                      style={{ marginLeft: "10px" }}
                      onClick={() => this.deleteUrlShortener(urlShortener)}
                      className="btn btn-danger"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    );
  }
}

export default ListUrlShortenerComponent;
