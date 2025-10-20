import axios from "axios";
const API_BASE = "http://localhost:5000/api";

export const getTftData = () => axios.get(`${API_BASE}/tft-data`);
