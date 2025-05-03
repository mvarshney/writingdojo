import React, { useState, useEffect } from 'react';

interface WritingEditorProps {
  initialContent?: string;
  onContentChange: (content: string, wordCount: number) => void;
  isReadOnly?: boolean;
}

const WritingEditor: React.FC<WritingEditorProps> = ({
  initialContent = '',
  onContentChange,
  isReadOnly = false,
}) => {
  const [content, setContent] = useState(initialContent);
  const [wordCount, setWordCount] = useState(0);

  useEffect(() => {
    const count = content.trim().split(/\s+/).filter(Boolean).length;
    setWordCount(count);
    onContentChange(content, count);
  }, [content, onContentChange]);

  return (
    <div className="w-full max-w-4xl mx-auto">
      <div className="mb-4 flex justify-between items-center">
        <div className="text-sm text-gray-600">
          Word Count: {wordCount}
        </div>
      </div>
      <div className="bg-white rounded-lg shadow-lg p-6">
        <textarea
          className="w-full h-96 p-4 text-gray-800 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          placeholder="Start writing your story here..."
          readOnly={isReadOnly}
        />
      </div>
    </div>
  );
};

export default WritingEditor; 