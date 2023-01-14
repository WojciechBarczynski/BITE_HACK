import axios from 'axios';

const URL = "http://127.0.0.1:5000";

const loginService = {
  login: (username) => {
    let formdata = new FormData();
    formdata.append("username", username);
    return axios.post(`${URL}/login`, formdata);
  }
};

export default loginService;