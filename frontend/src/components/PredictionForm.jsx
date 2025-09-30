import React, { useState } from 'react';
import { predictChurn } from '../services/api';
import ResultDisplay from './ResultDisplay';
import './PredictionForm.css';

const PredictionForm = ({ onBack }) => {
  const [formData, setFormData] = useState({
    gender: 'Male',
    SeniorCitizen: '0',
    Partner: 'No',
    Dependents: 'No',
    tenure: '',
    PhoneService: 'Yes',
    MultipleLines: 'No',
    InternetService: 'Fiber optic',
    OnlineSecurity: 'No',
    OnlineBackup: 'No',
    DeviceProtection: 'No',
    TechSupport: 'No',
    StreamingTV: 'No',
    StreamingMovies: 'No',
    Contract: 'Month-to-month',
    PaperlessBilling: 'Yes',
    PaymentMethod: 'Electronic check',
    MonthlyCharges: '',
    TotalCharges: ''
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      // Convert string numbers to appropriate types
      const dataToSend = {
        ...formData,
        SeniorCitizen: parseInt(formData.SeniorCitizen),
        tenure: parseInt(formData.tenure),
        MonthlyCharges: parseFloat(formData.MonthlyCharges),
        TotalCharges: parseFloat(formData.TotalCharges)
      };

      const response = await predictChurn(dataToSend);
      
      if (response.success) {
        setResult(response.prediction);
      } else {
        setError('Prediction failed. Please try again.');
      }
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred. Please check your input and try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setResult(null);
    setError(null);
  };

  if (result) {
    return <ResultDisplay result={result} onReset={handleReset} onBack={onBack} />;
  }

  return (
    <div className="form-container">
      <div className="form-wrapper">
        <button className="back-button" onClick={onBack}>
          ← Back
        </button>

        <h2 className="form-title">Customer Information</h2>
        <p className="form-subtitle">Enter customer details to predict churn probability</p>

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="prediction-form">
          {/* Demographics Section */}
          <div className="form-section">
            <h3 className="section-title">Demographics</h3>
            
            <div className="form-row">
              <div className="form-group">
                <label>Gender</label>
                <select name="gender" value={formData.gender} onChange={handleChange}>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                </select>
              </div>

              <div className="form-group">
                <label>Senior Citizen</label>
                <select name="SeniorCitizen" value={formData.SeniorCitizen} onChange={handleChange}>
                  <option value="0">No</option>
                  <option value="1">Yes</option>
                </select>
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Partner</label>
                <select name="Partner" value={formData.Partner} onChange={handleChange}>
                  <option value="Yes">Yes</option>
                  <option value="No">No</option>
                </select>
              </div>

              <div className="form-group">
                <label>Dependents</label>
                <select name="Dependents" value={formData.Dependents} onChange={handleChange}>
                  <option value="Yes">Yes</option>
                  <option value="No">No</option>
                </select>
              </div>
            </div>

            <div className="form-group">
              <label>Tenure (months) *</label>
              <input
                type="number"
                name="tenure"
                value={formData.tenure}
                onChange={handleChange}
                placeholder="e.g., 12"
                min="0"
                max="72"
                required
              />
            </div>
          </div>

          {/* Phone Services Section */}
          <div className="form-section">
            <h3 className="section-title">Phone Services</h3>
            
            <div className="form-row">
              <div className="form-group">
                <label>Phone Service</label>
                <select name="PhoneService" value={formData.PhoneService} onChange={handleChange}>
                  <option value="Yes">Yes</option>
                  <option value="No">No</option>
                </select>
              </div>

              <div className="form-group">
                <label>Multiple Lines</label>
                <select name="MultipleLines" value={formData.MultipleLines} onChange={handleChange}>
                  <option value="Yes">Yes</option>
                  <option value="No">No</option>
                  <option value="No phone service">No phone service</option>
                </select>
              </div>
            </div>
          </div>

          {/* Internet Services Section */}
          <div className="form-section">
            <h3 className="section-title">Internet Services</h3>
            
            <div className="form-group">
              <label>Internet Service</label>
              <select name="InternetService" value={formData.InternetService} onChange={handleChange}>
                <option value="DSL">DSL</option>
                <option value="Fiber optic">Fiber optic</option>
                <option value="No">No</option>
              </select>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Online Security</label>
                <select name="OnlineSecurity" value={formData.OnlineSecurity} onChange={handleChange}>
                  <option value="Yes">Yes</option>
                  <option value="No">No</option>
                  <option value="No internet service">No internet service</option>
                </select>
              </div>

              <div className="form-group">
                <label>Online Backup</label>
                <select name="OnlineBackup" value={formData.OnlineBackup} onChange={handleChange}>
                  <option value="Yes">Yes</option>
                  <option value="No">No</option>
                  <option value="No internet service">No internet service</option>
                </select>
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Device Protection</label>
                <select name="DeviceProtection" value={formData.DeviceProtection} onChange={handleChange}>
                  <option value="Yes">Yes</option>
                  <option value="No">No</option>
                  <option value="No internet service">No internet service</option>
                </select>
              </div>

              <div className="form-group">
                <label>Tech Support</label>
                <select name="TechSupport" value={formData.TechSupport} onChange={handleChange}>
                  <option value="Yes">Yes</option>
                  <option value="No">No</option>
                  <option value="No internet service">No internet service</option>
                </select>
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Streaming TV</label>
                <select name="StreamingTV" value={formData.StreamingTV} onChange={handleChange}>
                  <option value="Yes">Yes</option>
                  <option value="No">No</option>
                  <option value="No internet service">No internet service</option>
                </select>
              </div>

              <div className="form-group">
                <label>Streaming Movies</label>
                <select name="StreamingMovies" value={formData.StreamingMovies} onChange={handleChange}>
                  <option value="Yes">Yes</option>
                  <option value="No">No</option>
                  <option value="No internet service">No internet service</option>
                </select>
              </div>
            </div>
          </div>

          {/* Billing Section */}
          <div className="form-section">
            <h3 className="section-title">Billing Information</h3>
            
            <div className="form-group">
              <label>Contract Type</label>
              <select name="Contract" value={formData.Contract} onChange={handleChange}>
                <option value="Month-to-month">Month-to-month</option>
                <option value="One year">One year</option>
                <option value="Two year">Two year</option>
              </select>
            </div>

            <div className="form-group">
              <label>Paperless Billing</label>
              <select name="PaperlessBilling" value={formData.PaperlessBilling} onChange={handleChange}>
                <option value="Yes">Yes</option>
                <option value="No">No</option>
              </select>
            </div>

            <div className="form-group">
              <label>Payment Method</label>
              <select name="PaymentMethod" value={formData.PaymentMethod} onChange={handleChange}>
                <option value="Electronic check">Electronic check</option>
                <option value="Mailed check">Mailed check</option>
                <option value="Bank transfer (automatic)">Bank transfer (automatic)</option>
                <option value="Credit card (automatic)">Credit card (automatic)</option>
              </select>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Monthly Charges ($) *</label>
                <input
                  type="number"
                  name="MonthlyCharges"
                  value={formData.MonthlyCharges}
                  onChange={handleChange}
                  placeholder="e.g., 85.50"
                  step="0.01"
                  min="0"
                  required
                />
              </div>

              <div className="form-group">
                <label>Total Charges ($) *</label>
                <input
                  type="number"
                  name="TotalCharges"
                  value={formData.TotalCharges}
                  onChange={handleChange}
                  placeholder="e.g., 1020.00"
                  step="0.01"
                  min="0"
                  required
                />
              </div>
            </div>
          </div>

          <button type="submit" className="submit-button" disabled={loading}>
            {loading ? 'Predicting...' : 'Predict Churn'}
          </button>
        </form>
      </div>
    </div>
  );
};

export default PredictionForm;