import React from 'react';
import { Brand,CTA,Navbar } from './components';
import {Footer, Blog, Posibility, Features, WhatGPT3, Header} from "./containers";
import './App.css'

const App = () => {
  return (
    <div className="App">
        <div className='gradient__bg'>
            <Navbar />
            <Header />
          </div>
          <Brand />
          <WhatGPT3 />
          <Features />
          <Posibility />
          <CTA />
          <Blog />
          <Footer />
    </div>
  )
}
export default App