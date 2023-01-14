import React from 'react';
import '../style/main.css';
import NavbarComponent from './navbar';
import HomeComponent from './home';

const MainComponent = () => {
    return (
        <>
            <NavbarComponent />
            <HomeComponent />   
        </>
    );
};

export default MainComponent;