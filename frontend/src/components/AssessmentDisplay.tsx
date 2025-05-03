import React from 'react';

interface AssessmentDisplayProps {
  gradeLevel: string;
  grammarScore: string;
  structureScore: string;
  vocabularyScore: string;
  feedback: string;
}

const AssessmentDisplay: React.FC<AssessmentDisplayProps> = ({
  gradeLevel,
  grammarScore,
  structureScore,
  vocabularyScore,
  feedback,
}) => {
  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <h3 className="text-xl font-bold text-gray-800 mb-4">Assessment Results</h3>
      
      <div className="grid grid-cols-2 gap-4 mb-6">
        <div className="bg-gray-50 p-4 rounded-lg">
          <div className="text-sm font-semibold text-gray-500">Grade Level</div>
          <div className="text-lg font-bold text-gray-800">{gradeLevel}</div>
        </div>
        
        <div className="bg-gray-50 p-4 rounded-lg">
          <div className="text-sm font-semibold text-gray-500">Grammar</div>
          <div className="text-lg font-bold text-gray-800">{grammarScore}</div>
        </div>
        
        <div className="bg-gray-50 p-4 rounded-lg">
          <div className="text-sm font-semibold text-gray-500">Structure</div>
          <div className="text-lg font-bold text-gray-800">{structureScore}</div>
        </div>
        
        <div className="bg-gray-50 p-4 rounded-lg">
          <div className="text-sm font-semibold text-gray-500">Vocabulary</div>
          <div className="text-lg font-bold text-gray-800">{vocabularyScore}</div>
        </div>
      </div>
      
      <div>
        <div className="text-sm font-semibold text-gray-500 mb-2">Feedback</div>
        <div className="bg-gray-50 p-4 rounded-lg">
          <p className="text-gray-800 whitespace-pre-wrap">{feedback}</p>
        </div>
      </div>
    </div>
  );
};

export default AssessmentDisplay; 