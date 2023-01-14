import React from 'react';
import NavbarComponent from './navbar';
import '../style/home.css';
import TaskComponent from './task';
import ButtonsComponent from './buttons';
const HomeComponent = () => {
    return (
        <div className='conteiner'>
            <TaskComponent/>
            <ButtonsComponent/>
        </div>
    );
};

export default HomeComponent;