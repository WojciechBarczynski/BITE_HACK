import React, { useEffect, useState } from 'react';
import NavbarComponent from './navbar';
import '../style/home.css';
import TaskComponent from './task';
import { useNavigate } from 'react-router-dom';

const HomeComponent = () => {
    const navigate = useNavigate();
    const [fixTime, setFixTime] = useState(null);

    useEffect(() => {
        if(localStorage.getItem("userid") == null) {
            navigate("/login");
        }
    }, [])

    const fixStuff = () => {
        setFixTime(Date.now())
    }

    return (
        <div className='conteiner'>
            <NavbarComponent fixTime={fixTime} />
            <TaskComponent fixStuff={fixStuff} />
        </div>
    );
};

export default HomeComponent;