import axios from 'axios';

const URL = "http://127.0.0.1:5000";

const userInfoService = {
    getUserInfo: (userId) => {
      return axios.get(`${URL}/userinfo?userid=${userId}`);
    }
  };
  
  export default userInfoService;