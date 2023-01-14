import axios from 'axios';

const URL = "http://127.0.0.1:5000";

const taskService = {
  generate: () => {
    return axios.get(`${URL}/question?userid=${localStorage.getItem("userid")}`);
  }
};

export default taskService;