import axios from 'axios';

// Base URL for API - change this to your backend URL
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Health check
export const checkHealth = async () => {
  try {
    const response = await api.get('/api/health');
    return response.data;
  } catch (error) {
    console.error('Health check failed:', error);
    throw error;
  }
};

// Get feature information
export const getFeatures = async () => {
  try {
    const response = await api.get('/api/features');
    return response.data;
  } catch (error) {
    console.error('Failed to get features:', error);
    throw error;
  }
};

// Make prediction
export const predictChurn = async (customerData) => {
  try {
    const response = await api.post('/api/predict', customerData);
    return response.data;
  } catch (error) {
    console.error('Prediction failed:', error);
    throw error;
  }
};

// Batch prediction
export const predictChurnBatch = async (customersData) => {
  try {
    const response = await api.post('/api/predict/batch', {
      customers: customersData
    });
    return response.data;
  } catch (error) {
    console.error('Batch prediction failed:', error);
    throw error;
  }
};

export default api;