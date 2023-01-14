import axios from 'axios';

const URL = "";

const loginService = {
  login: (username) => {
    return axios.post(`${URL}/login`, {
        username: username
    });
  }
};

export default loginService;