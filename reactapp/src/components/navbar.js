import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../style/navbar.css';

const NavbarComponent = () => {
    const navigate = useNavigate();
    const [loggedIn, setLoggedIn] = useState(false);

    useEffect(() => {
        if(localStorage.getItem("userid") != null) setLoggedIn(true)
        else setLoggedIn(false)
    })
    
    const onLogout = () => {
        localStorage.removeItem("userid");
        navigate("/login");
    }

    return (
        <div className='navbarConteiner'>
            <div className='name'>LevelMind</div>
            {loggedIn ? <div onClick={onLogout} className='section'>Wyloguj się!</div> : <></>}
        </div>
    );
};

export default NavbarComponent;