import React, { Component } from 'react'
import UrlShortenerService from '../services/UrlShortenerService'

class ListUrlShortenerComponent extends Component {
    constructor(props) {
        super(props)

        this.state = {
                urlShorteners: []
        }
        this.addUrlShortener = this.addUrlShortener.bind(this);
        this.editUrlShortener = this.editUrlShortener.bind(this);
        this.deleteUrlShortener = this.deleteUrlShortener.bind(this);
    }

    deleteUrlShortener(id){
        UrlShortenerService.deleteUrlShortenerById(id).then( res => {
            this.setState({urlShorteners: this.state.urlShorteners.filter(urlShortener => urlShortener.id !== id)});
        });
    }
    viewUrlShortener(id){
        this.props.history.push(`/view-url-shortener/${id}`);
    }
    editUrlShortener(id){
        this.props.history.push(`/update-url-shortener/${id}`);
    }

    componentDidMount(){
        UrlShortenerService.getUrlShortener().then((res) => {
            if (res.data){
                this.setState({ urlShorteners: res.data});
            }
        });
        
    }

    addUrlShortener(){
        this.props.history.push('/add-url-shortener');
    }

    render() {
        return (
            <div>
                 <h2 className="text-center">Url Shortener List</h2>
                 <div className = "row">
                    <button className="btn btn-primary" onClick={this.addUrlShortener}> Add UrlShortener</button>
                 </div>
                 <br></br>
                 <div className = "row">
                        <table className = "table table-striped table-bordered">

                            <thead>
                                <tr>
                                    <th> Url Shortener Id</th>
                                    <th> Url Address</th>
                                    <th> Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {
                                    this.state.urlShorteners.map(
                                        urlShortener => 
                                        <tr key = {urlShortener.id}>
                                             <td> {urlShortener.id} </td>   
                                             <td> {urlShortener.urlAddress}</td>
                                             <td>
                                                 <button onClick={ () => this.editUrlShortener(urlShortener.id)} className="btn btn-info">Update </button>
                                                 <button style={{marginLeft: "10px"}} onClick={ () => this.deleteUrlShortener(urlShortener.id)} className="btn btn-danger">Delete </button>
                                                 <button style={{marginLeft: "10px"}} onClick={ () => this.viewUrlShortener(urlShortener.id)} className="btn btn-info">View </button>
                                             </td>
                                        </tr>
                                    )
                                }
                            </tbody>
                        </table>

                 </div>

            </div>
        )
    }
}

export default ListUrlShortenerComponent
