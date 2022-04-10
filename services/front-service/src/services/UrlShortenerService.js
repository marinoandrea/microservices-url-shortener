import axios from 'axios';

const URL_SHORTENER_API_BASE_URL = "http://localhost:5000";

class UrlShortenerService {

    getUrlShortener(){
        return axios.get(URL_SHORTENER_API_BASE_URL);
    }

    createUrlShortener(urlAddress){
        return axios.post(URL_SHORTENER_API_BASE_URL, urlAddress);
    }

    getUrlById(urlShortenerId){
        return axios.get(URL_SHORTENER_API_BASE_URL + '/' + urlShortenerId);
    }

    updateUrlShortener(urlAddress, urlShortenerId){
        return axios.put(URL_SHORTENER_API_BASE_URL + '/' + urlShortenerId, urlAddress);
    }

    deleteUrlShortenerById(urlShortenerId){
        return axios.delete(URL_SHORTENER_API_BASE_URL + '/' + urlShortenerId);
    }
}

export default new UrlShortenerService()
