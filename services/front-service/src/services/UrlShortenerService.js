import axios from "axios";
import { API_ENDPOINT } from "../config";

export const ROUTE = `${API_ENDPOINT}/shortener`;

var instance = axios.create({
  headers: {
    common: {
      // can be common or any other method
      Authorization: window.localStorage.token,
    },
  },
});

class UrlShortenerService {
  getUrlShortener() {
    return instance.get(ROUTE);
  }

  createUrlShortener(urlAddress) {
    return instance.post(ROUTE, { url: urlAddress });
  }

  getUrlById(urlShortenerId) {
    return instance.get(`${ROUTE}/${urlShortenerId}`);
  }

  updateUrlShortener(urlAddress, urlShortenerId) {
    return instance.put(`${ROUTE}/${urlShortenerId}`, {
      url: urlAddress,
    });
  }

  deleteUrlShortenerById(urlShortenerId) {
    return instance.delete(`${ROUTE}/${urlShortenerId}`);
  }
}

export default new UrlShortenerService();
