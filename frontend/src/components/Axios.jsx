import axios from "axios";

// const baseURL = 'http://127.0.0.1:8000/'

const isDevelopment = import.meta.env.MODE === 'development'
const baseURL2 = isDevelopment ? import.meta.env.VITE_API_BASE_URL_LOCAL : import.meta.env.VITE_API_BASE_URL_PROD

const AxiosInstance = axios.create({
    baseURL: baseURL2,
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        accept: 'application/json',
    }



})

export default AxiosInstance;