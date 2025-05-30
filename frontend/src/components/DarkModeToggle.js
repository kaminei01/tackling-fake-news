import React, { useEffect, useState } from 'react';

const DarkModeToggle = () => {
  const [darkMode, setDarkMode] = useState(() => {
    return localStorage.getItem('darkMode') === 'true' || false;
  });

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('darkMode', darkMode);
  }, [darkMode]);

  return (
    <button
      onClick={() => setDarkMode(!darkMode)}
      style={{
        padding: '8px 12px',
        borderRadius: '20px',
        border: '1px solid #ccc',
        cursor: 'pointer',
        background: darkMode ? '#333' : '#fff',
        color: darkMode ? '#fff' : '#000',
        transition: 'all 0.3s ease',
        position: 'fixed',
        top: '20px',
        right: '20px',
        zIndex: 1000,
      }}
      aria-label="Toggle Dark Mode"
    >
      {darkMode ? 'Light Mode' : 'Dark Mode'}
    </button>
  );
};

export default DarkModeToggle;
