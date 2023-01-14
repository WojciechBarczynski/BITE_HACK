import React from 'react';
import '../style/navbar.css';
const NavbarComponent = () => {
    return (
        <div className='navbarConteiner'>
            <div className='name'>Nazwa strony</div>
            <div className='section'>sekcja1</div>
            <div className='section'>sekcja2</div>
            <div className='section'>sekcja3</div>
            <div className='section'>sekcja4</div>
        </div>
    );
};

export default NavbarComponent;