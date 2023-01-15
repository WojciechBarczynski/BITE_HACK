import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import userInfoService from '../services/userInfoService';
import '../style/navbar.css';

const NavbarComponent = (props) => {
    const navigate = useNavigate();
    const [loggedIn, setLoggedIn] = useState(false);
    const [userName, setUserName] = useState("");
    const [userRating, setUserRating] = useState(0);

    useEffect(() => {
        if(localStorage.getItem("userid") != null) {
            userInfoService.getUserInfo(localStorage.getItem("userid")).then((res) => {
                setLoggedIn(true);
                setUserName(res.data.username);
                setUserRating(res.data.userrating);
            })
        }
        else setLoggedIn(false)
    }, [])

    useEffect(() => {
        userInfoService.getUserInfo(localStorage.getItem("userid")).then((res) => {
            setUserRating(res.data.userrating);
        })
    }, [props.fixTime])
    
    const onLogout = () => {
        localStorage.removeItem("userid");
        navigate("/login");
    }

    return (
        <div className='navbarConteiner'>
            <div className='name'>LevelMind</div>
            <div className="smallFlex">
                <div>
                    {loggedIn ? <div>{userName} <b>(👑 {userRating})</b>&nbsp;&nbsp;&nbsp;</div> : <></>}
                </div>
                <div>
                    {loggedIn ? <div onClick={onLogout} className='section'>Wyloguj się!</div> : <></>}
                </div>
            </div>
            
        </div>
    );
};

export default NavbarComponent;