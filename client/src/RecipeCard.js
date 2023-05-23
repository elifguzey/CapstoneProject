import React, { useState } from 'react'
import { useNavigate } from "react-router-dom";

function RecipeCard(props) {
    return (
        <div className="card">
            <div className="card-image">
                <figure className="image is-4by3">
                    <img src={props.image} alt="Placeholder image" />
                </figure>
            </div>
            <div className="card-content">
                <div className="media">
                    <div className="media-content">
                        <p className="title is-4">{props.title}</p>
                    </div>
                </div>

                <div className="content">
                    <p>{props.description}</p>
                </div>
            </div>
        </div>
    )
}

export default RecipeCard;