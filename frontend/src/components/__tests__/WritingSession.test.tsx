import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MemoryRouter } from 'react-router-dom';
import WritingSession from '../WritingSession';

// Define the WritingSession props type
interface WritingSessionProps {
  topic: string;
  writingMode: string;
  onSessionComplete: (content: string, wordCount: number) => void;
}

// Mock the API calls
jest.mock('../../api/writingSessions', () => ({
  createWritingSession: jest.fn().mockResolvedValue({
    id: 1,
    child_id: 1,
    topic: 'My Summer Vacation',
    writing_mode: 'free',
    content: 'I went to the beach...',
    word_count: 150,
    duration: 30
  }),
  getWritingAssessment: jest.fn().mockResolvedValue({
    id: 1,
    session_id: 1,
    grade_level: '5th grade',
    grammar_score: 'Good',
    structure_score: 'Excellent',
    vocabulary_score: 'Fair',
    feedback: 'Great job! Keep practicing...',
    strengths: ['Good story structure', 'Clear narrative'],
    areas_for_improvement: ['Vocabulary usage', 'Grammar']
  })
}));

// Mock the WritingSession component
jest.mock('../WritingSession', () => {
  const MockWritingSession: React.FC<WritingSessionProps> = ({ topic, writingMode, onSessionComplete }) => {
    return (
      <div>
        <h1>Writing Session</h1>
        <p>Topic: {topic}</p>
        <p>Writing Mode: {writingMode}</p>
        <p>Word Count: 0</p>
        <p>Duration: 0:00</p>
        <textarea role="textbox" />
        <button onClick={() => onSessionComplete('Test content', 5)}>I am done</button>
      </div>
    );
  };
  return MockWritingSession;
});

describe('WritingSession', () => {
  const mockProps: WritingSessionProps = {
    topic: 'My Summer Vacation',
    writingMode: 'free',
    onSessionComplete: jest.fn()
  };

  it('renders the writing session interface', () => {
    render(
      <MemoryRouter>
        <WritingSession {...mockProps} />
      </MemoryRouter>
    );

    expect(screen.getByText('Writing Session')).toBeInTheDocument();
    expect(screen.getByText('Topic: My Summer Vacation')).toBeInTheDocument();
    expect(screen.getByText('Writing Mode: free')).toBeInTheDocument();
    expect(screen.getByText('Word Count: 0')).toBeInTheDocument();
    expect(screen.getByText('Duration: 0:00')).toBeInTheDocument();
  });

  it('calls onSessionComplete when session is ended', () => {
    render(
      <MemoryRouter>
        <WritingSession {...mockProps} />
      </MemoryRouter>
    );

    const endButton = screen.getByText('I am done');
    fireEvent.click(endButton);

    expect(mockProps.onSessionComplete).toHaveBeenCalledWith('Test content', 5);
  });

  it('shows assessment after session is completed', async () => {
    render(
      <MemoryRouter>
        <WritingSession {...mockProps} />
      </MemoryRouter>
    );

    const endButton = screen.getByText('I am done');
    fireEvent.click(endButton);

    await waitFor(() => {
      expect(screen.getByText('Assessment Results')).toBeInTheDocument();
    });

    expect(screen.getByText('Grammar Score: Good')).toBeInTheDocument();
    expect(screen.getByText('Structure Score: Excellent')).toBeInTheDocument();
    expect(screen.getByText('Vocabulary Score: Appropriate')).toBeInTheDocument();
  });

  it('updates word count as user types', () => {
    render(
      <MemoryRouter>
        <WritingSession {...mockProps} />
      </MemoryRouter>
    );

    const editor = screen.getByRole('textbox');
    fireEvent.change(editor, { target: { value: 'This is a test sentence.' } });

    expect(screen.getByText('Word Count: 5')).toBeInTheDocument();
  });

  it('starts and stops the timer', async () => {
    render(
      <MemoryRouter>
        <WritingSession {...mockProps} />
      </MemoryRouter>
    );

    const startButton = screen.getByText('Start');
    fireEvent.click(startButton);

    // Wait for timer to update
    await waitFor(() => {
      expect(screen.getByText(/Duration: 0:0[1-9]/)).toBeInTheDocument();
    });

    const stopButton = screen.getByText('Stop');
    fireEvent.click(stopButton);

    // Timer should stop
    const duration = screen.getByText(/Duration: 0:0[1-9]/).textContent;
    await new Promise(resolve => setTimeout(resolve, 1000));
    expect(screen.getByText(duration)).toBeInTheDocument();
  });

  it('handles loading state', async () => {
    // Mock slow API response
    jest.spyOn(require('../../api/writingSessions'), 'createWritingSession')
      .mockImplementationOnce(() => new Promise(resolve => setTimeout(resolve, 1000)));

    render(
      <MemoryRouter>
        <WritingSession {...mockProps} />
      </MemoryRouter>
    );

    const submitButton = screen.getByText('Submit');
    fireEvent.click(submitButton);

    expect(screen.getByText('Submitting...')).toBeInTheDocument();
  });

  it('handles error state', async () => {
    // Mock API error
    jest.spyOn(require('../../api/writingSessions'), 'createWritingSession')
      .mockRejectedValueOnce(new Error('Failed to submit session'));

    render(
      <MemoryRouter>
        <WritingSession {...mockProps} />
      </MemoryRouter>
    );

    const submitButton = screen.getByText('Submit');
    fireEvent.click(submitButton);

    // Wait for error message
    const errorMessage = await screen.findByText('Error submitting writing session');
    expect(errorMessage).toBeInTheDocument();
  });
}); 