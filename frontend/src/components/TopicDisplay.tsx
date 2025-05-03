import React from 'react';

interface TopicDisplayProps {
  topic: string;
  writingMode: string;
}

const TopicDisplay: React.FC<TopicDisplayProps> = ({ topic, writingMode }) => {
  return (
    <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
      <div className="flex flex-col space-y-2">
        <div className="text-sm font-semibold text-gray-500 uppercase tracking-wider">
          Writing Mode
        </div>
        <div className="text-xl font-bold text-gray-800 capitalize">
          {writingMode}
        </div>
        <div className="text-sm font-semibold text-gray-500 uppercase tracking-wider mt-4">
          Topic
        </div>
        <div className="text-xl font-bold text-gray-800">
          {topic}
        </div>
      </div>
    </div>
  );
};

export default TopicDisplay; 