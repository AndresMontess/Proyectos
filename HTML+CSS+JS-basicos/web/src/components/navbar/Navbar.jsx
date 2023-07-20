import React from 'react';
import {RiMenu3Line, RiCLoseLin} from 'react-icons/ri';
import logo from '../../assets/assets/logo.svg';
import './navbar.css';
const navbar = () => {
  return (
    <div className='gpt3__navbar'>
      <div className='gpt3__navbar-links'>
        <div className='gpt3_navbar_links_logo'>
          <img src={logo} alt="logo" />
        </div>
      </div>
    </div>
  )
}

export default navbar