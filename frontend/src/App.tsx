import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import WritingSession from './components/WritingSession';
import TopBar from './components/TopBar';
import './App.css';

function App() {
  const [selectedChild, setSelectedChild] = useState('adhvik');
  const handleSessionComplete = (content: string, wordCount: number) => {
    console.log('Session completed:', { content, wordCount });
    // TODO: Send to backend for assessment
  };

  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <TopBar selectedChild={selectedChild} onChildSelect={setSelectedChild} />
        
        <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
          <Routes>
            <Route
              path="/"
              element={
                <div className="text-center py-12">
                  <h1 className="text-3xl font-bold text-gray-800 mb-4">
                    Welcome to Writing Dojo
                  </h1>
                  <p className="text-gray-600 mb-8">
                    Select a child and start writing!
                  </p>
                  <Link
                    to="/writing"
                    className="inline-block bg-blue-500 hover:bg-blue-600 text-white px-6 py-3 rounded-lg font-medium transition-colors"
                  >
                    Start Writing
                  </Link>
                </div>
              }
            />
            <Route
              path="/writing"
              element={
                <WritingSession
                  topic="A day in the life of a superhero"
                  writingMode="creative"
                  onSessionComplete={handleSessionComplete}
                />
              }
            />
            <Route
              path="/progress"
              element={
                <div className="text-center py-12">
                  <h1 className="text-3xl font-bold text-gray-800 mb-4">
                    Progress for {selectedChild === 'adhvik' ? 'Adhvik' : 'Anika'}
                  </h1>
                  <p className="text-gray-600">
                    Progress tracking coming soon...
                  </p>
                </div>
              }
            />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
