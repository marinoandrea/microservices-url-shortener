import React, { Component } from 'react'
import UrlShortenerService from '../services/UrlShortenerService';

class UpdateUrlShortenerComponent extends Component {
    constructor(props) {
        super(props)

        this.state = {
            id: this.props.match.params.id,
            urlAddress: ''
        }
        this.changeUrlAddressHandler = this.changeUrlAddressHandler.bind(this);
        this.updateUrlShortener = this.updateUrlShortener.bind(this);
    }

    componentDidMount(){
        UrlShortenerService.getUrlById(this.state.id).then( (res) =>{
            let urlShortener = res.data;
            this.setState({urlAddress: urlShortener.urlAddress,
                id: urlShortener.id,
            });
        });
    }

    updateUrlShortener = (e) => {
        e.preventDefault();
        let urlShortener = {urlAddress: this.state.urlAddress, id: this.state.id};
        console.log('urlShortener => ' + JSON.stringify(urlShortener));
        console.log('id => ' + JSON.stringify(this.state.id));
        UrlShortenerService.updateUrlShortener(urlShortener.urlAddress, this.state.id).then( res => {
            this.props.history.push('/url-shortener-list');
        });
    }
    
    changeUrlAddressHandler= (event) => {
        this.setState({urlAddress: event.target.value});
    }

    cancel(){
        this.props.history.push('/url-shortener-list');
    }

    render() {
        return (
            <div>
                <br></br>
                   <div className = "container">
                        <div className = "row">
                            <div className = "card col-md-6 offset-md-3 offset-md-3">
                                <h3 className="text-center">Update Url Shortener</h3>
                                <div className = "card-body">
                                    <form>
                                        <div className = "form-group">
                                            <label> Url Address: </label>
                                            <input placeholder="Url Address" name="urlAddress" className="form-control" 
                                                value={this.state.urlAddress} onChange={this.changeUrlAddressHandler}/>
                                        </div>
                                    

                                        <button className="btn btn-success" onClick={this.updateUrlShortener}>Save</button>
                                        <button className="btn btn-danger" onClick={this.cancel.bind(this)} style={{marginLeft: "10px"}}>Cancel</button>
                                    </form>
                                </div>
                            </div>
                        </div>

                   </div>
            </div>
        )
    }
}

export default UpdateUrlShortenerComponent
