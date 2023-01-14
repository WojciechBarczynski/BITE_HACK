import React from 'react';
import '../style/buttons.css';
const ButtonsComponent = () => {
    const {useEffect, useState} = React
    const [inputValue, setInputValue] = useState("")

    return (
        <div className='buttonsContainer'>
            <input type = "text" className='inpucik' value={inputValue} onInput={(event) => {
                    setInputValue(event.value)
                }}></input>
            <div className='buttons'>
                <div className='buttonik' onClick = {() => {
                    
                }}>Wylosuj pytanie</div>
                <div className='buttonik' onClick ={()=> {
                    setInputValue("")
                }}>Wyślij</div>
            </div>
        </div>
    );
};

export default ButtonsComponent;