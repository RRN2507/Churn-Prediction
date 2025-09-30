import React from 'react';
import './ResultDisplay.css';

const ResultDisplay = ({ result, onReset, onBack }) => {
  const isChurn = result.churn === 'Yes';
  const churnPercentage = (result.churn_probability * 100).toFixed(1);
  const confidence = (result.confidence * 100).toFixed(1);

  return (
    <div className="result-container">
      <div className="result-wrapper">
        <button className="back-button" onClick={onBack}>
          ← Back to Home
        </button>

        <div className={`result-card ${isChurn ? 'churn' : 'no-churn'}`}>
          <div className="result-icon">
            {isChurn ? '⚠️' : '✅'}
          </div>

          <h2 className="result-title">
            {isChurn ? 'High Churn Risk' : 'Low Churn Risk'}
          </h2>

          <p className="result-message">
            {isChurn 
              ? 'This customer is likely to churn. Consider retention strategies.'
              : 'This customer is likely to stay. Keep maintaining good service.'}
          </p>

          <div className="probability-section">
            <div className="probability-card">
              <h3>Churn Probability</h3>
              <div className="probability-value">
                {churnPercentage}%
              </div>
              <div className="probability-bar">
                <div 
                  className="probability-fill churn-fill" 
                  style={{ width: `${churnPercentage}%` }}
                ></div>
              </div>
            </div>

            <div className="probability-card">
              <h3>Confidence Level</h3>
              <div className="probability-value">
                {confidence}%
              </div>
              <div className="probability-bar">
                <div 
                  className="probability-fill confidence-fill" 
                  style={{ width: `${confidence}%` }}
                ></div>
              </div>
            </div>
          </div>

          {isChurn && (
            <div className="recommendations">
              <h3>Recommended Actions</h3>
              <ul>
                <li>Reach out to the customer proactively</li>
                <li>Offer personalized retention incentives</li>
                <li>Address service quality concerns</li>
                <li>Consider contract upgrade options</li>
                <li>Provide additional support services</li>
              </ul>
            </div>
          )}

          <div className="action-buttons">
            <button className="secondary-button" onClick={onReset}>
              Make Another Prediction
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultDisplay;