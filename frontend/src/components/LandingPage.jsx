import React from 'react';
import './LandingPage.css';

const LandingPage = ({ onGetStarted }) => {
  return (
    <div className="landing-container">
      <div className="landing-content">
        <div className="hero-section">
          <h1 className="main-title">
            Customer Churn Prediction
          </h1>
          <p className="subtitle">
            Predict customer churn with advanced machine learning
          </p>
          <p className="description">
            Our AI-powered system analyzes customer data to predict the likelihood 
            of churn, helping you take proactive measures to retain valuable customers.
          </p>
          
          <button className="cta-button" onClick={onGetStarted}>
            Get Started
            <span className="arrow">→</span>
          </button>
        </div>

        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">🎯</div>
            <h3>Accurate Predictions</h3>
            <p>Machine learning models trained on thousands of customer records</p>
          </div>
          
          <div className="feature-card">
            <div className="feature-icon">⚡</div>
            <h3>Instant Results</h3>
            <p>Get churn predictions in real-time with probability scores</p>
          </div>
          
          <div className="feature-card">
            <div className="feature-icon">📊</div>
            <h3>Data-Driven Insights</h3>
            <p>Make informed decisions based on comprehensive analysis</p>
          </div>
          
          <div className="feature-card">
            <div className="feature-icon">🔒</div>
            <h3>Secure & Reliable</h3>
            <p>Your data is processed securely with industry standards</p>
          </div>
        </div>

        <div className="stats-section">
          <div className="stat">
            <h2>95%</h2>
            <p>Accuracy</p>
          </div>
          <div className="stat">
            <h2>7000+</h2>
            <p>Training Samples</p>
          </div>
          <div className="stat">
            <h2>&lt;1s</h2>
            <p>Prediction Time</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;