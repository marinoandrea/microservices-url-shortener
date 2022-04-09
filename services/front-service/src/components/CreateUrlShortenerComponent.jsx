import React, { Component } from 'react'
import UrlShortenerService from '../services/UrlShortenerService';

class CreateUrlShortenerComponent extends Component {
    constructor(props) {
        super(props)

        this.state = {
            // step 2
            id: this.props.match.params.id,
            url: '',
        }
        this.changeUrlAddressHandler = this.changeUrlAddressHandler.bind(this);
        this.saveUrlShortener = this.saveUrlShortener.bind(this);
    }

    // step 3
    componentDidMount(){

        // step 4
        if(this.state.id === '_add'){
            return
        }else{
            UrlShortenerService.getUrlById(this.state.id).then( (res) =>{
                let urlShortener = res.data;
                this.setState({url: urlShortener.url
                });
            });
        }        
    }
    saveUrlShortener = (e) => {
        e.preventDefault();
        let urlShortener = {url: this.state.url};
        console.log('urlShortener => ' + JSON.stringify(urlShortener));

        // step 5

        UrlShortenerService.createUrlShortener(urlShortener).then(res =>{
            this.props.history.push('/url-shortener-list');
        });
        
    }
    
    changeUrlAddressHandler= (event) => {
        this.setState({url: event.target.value});
    }

    cancel(){
        this.props.history.push('/url-shortener-list');
    }

    getTitle(){
        if(this.state.id === '_add'){
            return <h3 className="text-center">Add URL Shortener</h3>
        }else{
            return <h3 className="text-center">Update URL Shortener</h3>
        }
    }
    render() {
        return (
            <div>
                <br></br>
                   <div className = "container">
                        <div className = "row">
                            <div className = "card col-md-6 offset-md-3 offset-md-3">
                                {
                                    this.getTitle()
                                }
                                <div className = "card-body">
                                    <form>
                                        <div className = "form-group">
                                            <label> Url Address: </label>
                                            <input placeholder="Url Address" name="url" className="form-control" 
                                                value={this.state.url} onChange={this.changeUrlAddressHandler}/>
                                        </div>
                                        <button className="btn btn-success" onClick={this.saveUrlShortener}>Save</button>
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

export default CreateUrlShortenerComponent
