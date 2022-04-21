import axios from "axios";

export const URL_SHORTENER_API_BASE_URL = "/userservice/";

class UserService {
  login(username,password) {
    return axios.post(URL_SHORTENER_API_BASE_URL+"users/login",{ username: username,password:password });
  }

  createUser(username,password) {
    return axios.post(URL_SHORTENER_API_BASE_URL+"users",{ username: username,password:password });
  }
}

export default new UserService();
