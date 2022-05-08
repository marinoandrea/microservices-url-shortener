import axios from "axios";
import { API_ENDPOINT } from "../config";

export const ROUTE = `${API_ENDPOINT}/auth`;

class UserService {
  login(username, password) {
    return axios.post(`${ROUTE}/users/login`, {
      username: username,
      password: password,
    });
  }

  createUser(username, password) {
    return axios.post(`${ROUTE}/users/login`, {
      username: username,
      password: password,
    });
  }
}

export default new UserService();
