import React, { useState, useEffect } from 'react';

interface TimerProps {
  duration: number; // in minutes
  onTimeUp: () => void;
  isActive: boolean;
}

const Timer: React.FC<TimerProps> = ({ duration, onTimeUp, isActive }) => {
  const [timeLeft, setTimeLeft] = useState(duration * 60); // convert to seconds

  useEffect(() => {
    let interval: NodeJS.Timeout;

    if (isActive && timeLeft > 0) {
      interval = setInterval(() => {
        setTimeLeft((prevTime) => {
          if (prevTime <= 1) {
            clearInterval(interval);
            onTimeUp();
            return 0;
          }
          return prevTime - 1;
        });
      }, 1000);
    }

    return () => clearInterval(interval);
  }, [isActive, timeLeft, onTimeUp]);

  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;

  return (
    <div className="flex items-center justify-center">
      <div className="text-2xl font-bold text-gray-800">
        {minutes.toString().padStart(2, '0')}:
        {seconds.toString().padStart(2, '0')}
      </div>
    </div>
  );
};

export default Timer; 