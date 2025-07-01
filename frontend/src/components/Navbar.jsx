import React from 'react';
import { Link } from 'react-router-dom';
import DarkModeToggle from './DarkModeToggle';

const Navbar = () => {
  return (
    <nav className="navbar">
      <h2>🧠 Fake News Detector</h2>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/analyze">Analyze</Link></li>
        <li><Link to="/feedback">Feedback</Link></li>
      </ul>
      <DarkModeToggle />
    </nav>
  );
};

export default Navbar;
