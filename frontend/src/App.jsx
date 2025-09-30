import React, { useState } from 'react';
import LandingPage from './components/LandingPage';
import PredictionForm from './components/PredictionForm';

function App() {
  const [currentPage, setCurrentPage] = useState('landing');

  const handleGetStarted = () => {
    setCurrentPage('prediction');
  };

  const handleBackToHome = () => {
    setCurrentPage('landing');
  };

  return (
    <div className="App">
      {currentPage === 'landing' ? (
        <LandingPage onGetStarted={handleGetStarted} />
      ) : (
        <PredictionForm onBack={handleBackToHome} />
      )}
    </div>
  );
}

export default App;