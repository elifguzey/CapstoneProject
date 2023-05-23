import React from "react";
import { NavLink } from 'react-router-dom'
import "./Navbar.css";

function Navbar() {

    return (
        <header className='header'>
            <NavLink className="button" exact to="/">HOME</NavLink>
            <NavLink className="button" exact to="/login">LOGIN</NavLink>
            <NavLink className="button" exact to="/signup">SIGNUP</NavLink>
        </header>
    )
}

export default Navbar;