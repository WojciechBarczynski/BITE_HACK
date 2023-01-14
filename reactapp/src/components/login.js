import React, { useEffect, useState } from 'react';
import { redirect, useNavigate } from 'react-router-dom';
import loginService from '../services/loginService';
import NavbarComponent from './navbar';


const LoginComponent = () => {
    const [loginInput, setLoginInput] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        let userid = localStorage.getItem("userid");
        console.log(userid)
        if(userid && userid != "") {
            navigate("/");
        }

    }, [])
    
    const onLogin = () => {
        loginService.login(loginInput).then((res) => {
            localStorage.setItem("userid", res.data.userid)
            navigate("/");
        })
    }

    return (
        <div className='conteiner'>
            <NavbarComponent/>
            <div>
            <input type="text" value={loginInput} 
                onChange={(e) => {setLoginInput(e.target.value)}} />
            <button onClick={onLogin}>Zaloguj się</button>
        </div>
        </div>
    );
};

export default LoginComponent;