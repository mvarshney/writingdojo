import React, { useState, useEffect } from 'react';

interface TimerProps {
  isActive: boolean;
}

const Timer: React.FC<TimerProps> = ({ isActive }) => {
  const [minutes, setMinutes] = useState(0);

  useEffect(() => {
    let interval: NodeJS.Timeout;

    if (isActive) {
      interval = setInterval(() => {
        setMinutes((prevMinutes) => prevMinutes + 1);
      }, 60000); // Update every minute (60,000 milliseconds)
    }

    return () => {
      if (interval) {
        clearInterval(interval);
      }
    };
  }, [isActive]);

  return (
    <div className="flex items-center justify-center">
      <div className="text-2xl font-bold text-gray-800">
        {minutes.toString().padStart(2, '0')}:00
      </div>
    </div>
  );
};

export default Timer; 