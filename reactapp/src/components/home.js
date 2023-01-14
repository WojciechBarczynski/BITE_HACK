import React from 'react';
import { useNavigate } from 'react-router-dom';

const HomeComponent = () => {
    const navigate = useNavigate();

    const onLogout = () => {
        localStorage.removeItem("userid");
        navigate("/login");
    }

    return (
        <div>
            Welcome!
            <button onClick={onLogout}>Wyloguj się</button>
        </div>
    );
};

export default HomeComponent;