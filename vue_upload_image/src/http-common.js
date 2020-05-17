import axios from "axios";

export default axios.create({
  baseURL: "http://52.188.26.68:80",
  headers: {
    "Content-type": "application/json"
  }
});
