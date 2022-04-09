import React, { Component } from 'react'
import UrlShortenerService from '../services/UrlShortenerService'

class ViewUrlShortenerComponent extends Component {
    constructor(props) {
        super(props)

        this.state = {
            id: this.props.match.params.id,
            urlShortener: {}
        }
    }

    componentDidMount(){
        UrlShortenerService.getUrlById(this.state.id).then( res => {
            this.setState({urlShortener: res.data});
        })
    }

    render() {
        return (
            <div>
                <br></br>
                <div className = "card col-md-6 offset-md-3">
                    <h3 className = "text-center"> View Url Shortener Details</h3>
                    <div className = "card-body">
                        <div className = "row">
                            <label> Url Address: </label>
                            <div> { this.state.urlShortener.urlAddress }</div>
                        </div>
                    </div>

                </div>
            </div>
        )
    }
}

export default ViewUrlShortenerComponent
