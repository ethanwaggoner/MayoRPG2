import axios from "axios";

const apiService = axios.create({
  baseURL: "http://localhost:5000/",
  withCredentials: true,
});

export default apiService;
