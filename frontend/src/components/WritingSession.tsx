import React, { useState } from 'react';
import WritingEditor from './WritingEditor';
import Timer from './Timer';
import TopicDisplay from './TopicDisplay';
import AssessmentDisplay from './AssessmentDisplay';

interface WritingSessionProps {
  topic: string;
  writingMode: string;
  duration: number;
  onSessionComplete: (content: string, wordCount: number) => void;
}

const WritingSession: React.FC<WritingSessionProps> = ({
  topic,
  writingMode,
  duration,
  onSessionComplete,
}) => {
  const [isActive, setIsActive] = useState(true);
  const [content, setContent] = useState('');
  const [wordCount, setWordCount] = useState(0);
  const [showAssessment, setShowAssessment] = useState(false);

  const handleContentChange = (newContent: string, newWordCount: number) => {
    setContent(newContent);
    setWordCount(newWordCount);
  };

  const handleTimeUp = () => {
    setIsActive(false);
    setShowAssessment(true);
    onSessionComplete(content, wordCount);
  };

  return (
    <div className="min-h-screen bg-gray-100 py-8 px-4">
      <div className="max-w-4xl mx-auto space-y-6">
        <div className="flex justify-between items-center">
          <h1 className="text-2xl font-bold text-gray-800">Writing Session</h1>
          <Timer
            duration={duration}
            onTimeUp={handleTimeUp}
            isActive={isActive}
          />
        </div>

        <TopicDisplay
          topic={topic}
          writingMode={writingMode}
        />

        <WritingEditor
          initialContent={content}
          onContentChange={handleContentChange}
          isReadOnly={!isActive}
        />

        {showAssessment && (
          <AssessmentDisplay
            gradeLevel="Appropriate"
            grammarScore="Good"
            structureScore="Excellent"
            vocabularyScore="Appropriate"
            feedback="Your writing shows good structure and vocabulary usage. Consider adding more descriptive details to make your story more engaging."
          />
        )}
      </div>
    </div>
  );
};

export default WritingSession; 