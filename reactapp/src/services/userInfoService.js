import axios from 'axios';

const URL = "http://127.0.0.1:5000";

const userInfoService = {
    getUserInfo: (userId) => {
      let formdata = new FormData();
      formdata.append("userId", userId);
      return axios.get(`${URL}/userinfo`, formdata);
    }
  };
  
  export default userInfoService;