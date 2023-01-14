import axios from 'axios';

const URL = "http://127.0.0.1:5000";

const answerService = {
    answer: (userid, taskid, answer) => {
      let formdata = new FormData();
      formdata.append("userid", userid);
      formdata.append("taskid", taskid);
      formdata.append("answer", answer);
      
      return axios.post(`${URL}/answer`, formdata);
    }
  };
  
  export default answerService;