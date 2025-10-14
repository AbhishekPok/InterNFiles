import { useState } from "react";
import React from "react";
import App from "../../App";

function Appx(){
  
    const[currentstate, setcurrentstate] = useState(() => {
        console.log("Runs only once when the component is being rendered.")
        return 0
    })
    function decrementcount(){
        setcurrentstate(previousState => previousState -1)
    }
    function incrementcount(){
        setcurrentstate(nextState => nextState + 1)
    }
    return(
        <>
        <button onClick={decrementcount}>-</button>
        <span>{currentstate}</span>
        <button onClick={incrementcount}>+</button>
        </>
    )

}

export default Appx