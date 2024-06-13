// src/axios.js

import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000',  // URL base do seu backend FastAPI
  timeout: 10000,  // Tempo limite da requisição (opcional)
});

export default instance;
