import axios from "axios";

export const URL_SHORTENER_API_BASE_URL = "/urlshortener";
var instance = axios.create({
    headers: {
        common: {        // can be common or any other method
            Authorization: window.localStorage.token
        }
    }
});

class UrlShortenerService {
  getUrlShortener() {
    return instance.get(URL_SHORTENER_API_BASE_URL);
  }

  createUrlShortener(urlAddress) {
    return instance.post(URL_SHORTENER_API_BASE_URL, { url: urlAddress });
  }

  getUrlById(urlShortenerId) {
    return instance.get(URL_SHORTENER_API_BASE_URL + "/" + urlShortenerId);
  }

  updateUrlShortener(urlAddress, urlShortenerId) {
    return instance.put(URL_SHORTENER_API_BASE_URL + "/" + urlShortenerId, {
      url: urlAddress,
    });
  }

  deleteUrlShortenerById(urlShortenerId) {
    return instance.delete(URL_SHORTENER_API_BASE_URL + "/" + urlShortenerId);
  }
}

export default new UrlShortenerService();
