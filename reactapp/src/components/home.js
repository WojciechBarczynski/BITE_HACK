import React from 'react';
import NavbarComponent from './navbar';
import '../style/home.css';
import TaskComponent from './task';
import ButtonsComponent from './buttons';
import { useNavigate } from 'react-router-dom';

const HomeComponent = () => {
    const navigate = useNavigate();

    const onLogout = () => {
        localStorage.removeItem("userid");
        navigate("/login");
    }

    return (
        <div className='conteiner'>
            <NavbarComponent/>
            <TaskComponent/>
            <ButtonsComponent/>
        </div>
    );
};

export default HomeComponent;