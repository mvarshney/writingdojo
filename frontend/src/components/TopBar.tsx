import React from 'react';
import { Link } from 'react-router-dom';

interface Child {
  id: string;
  name: string;
  gender: 'boy' | 'girl';
}

interface TopBarProps {
  selectedChild: string;
  onChildSelect: (childId: string) => void;
}

const TopBar: React.FC<TopBarProps> = ({ selectedChild, onChildSelect }) => {
  const children: Child[] = [
    { id: 'adhvik', name: 'Adhvik', gender: 'boy' },
    { id: 'anika', name: 'Anika', gender: 'girl' },
  ];

  return (
    <div className="bg-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Child Selection */}
          <div className="flex items-center space-x-4">
            <span className="text-gray-600 font-medium">I am...</span>
            {children.map((child) => (
              <button
                key={child.id}
                onClick={() => onChildSelect(child.id)}
                className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                  selectedChild === child.id
                    ? child.gender === 'boy'
                      ? 'bg-blue-500 text-white'
                      : 'bg-pink-500 text-white'
                    : 'bg-gray-100 text-gray-400 hover:bg-gray-200'
                }`}
              >
                {child.name}
              </button>
            ))}
          </div>

          {/* Navigation Links */}
          <div className="flex space-x-4">
            <Link
              to="/writing"
              className="flex items-center px-4 py-2 rounded-lg font-medium text-gray-700 hover:bg-gray-100 transition-colors"
            >
              <svg
                className="w-5 h-5 mr-2"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
                />
              </svg>
              Start Writing
            </Link>
            <Link
              to="/progress"
              className="flex items-center px-4 py-2 rounded-lg font-medium text-gray-700 hover:bg-gray-100 transition-colors"
            >
              <svg
                className="w-5 h-5 mr-2"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                />
              </svg>
              Show Progress
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TopBar; 