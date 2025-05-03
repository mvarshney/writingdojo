import React from 'react';
import WritingSession from './components/WritingSession';
import './App.css';

function App() {
  const handleSessionComplete = (content: string, wordCount: number) => {
    console.log('Session completed:', { content, wordCount });
    // TODO: Send to backend for assessment
  };

  return (
    <div className="App">
      <WritingSession
        topic="A day in the life of a superhero"
        writingMode="creative"
        duration={30}
        onSessionComplete={handleSessionComplete}
      />
    </div>
  );
}

export default App;
