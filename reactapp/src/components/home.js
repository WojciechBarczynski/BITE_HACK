import React, { useEffect } from 'react';
import NavbarComponent from './navbar';
import '../style/home.css';
import TaskComponent from './task';
import { useNavigate } from 'react-router-dom';

const HomeComponent = () => {
    const navigate = useNavigate();

    useEffect(() => {
        if(localStorage.getItem("userid") == null) {
            navigate("/login");
        }
    }, [])

    return (
        <div className='conteiner'>
            <NavbarComponent/>
            <TaskComponent/>
        </div>
    );
};

export default HomeComponent;