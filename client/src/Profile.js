import React from 'react'
import { useNavigate } from "react-router-dom";

function Profile({ currentUser, onLogout }) {

    const navigate = useNavigate();



    return (

        <div className="Profile">
            <div>
                <h2><b>Logged in as:</b></h2>
            </div>
            <br/>
            <div>Name: {currentUser.username}</div>
            <div>Email: {currentUser.email}</div>
            <br/>
        </div>
    )
}

export default Profile;

