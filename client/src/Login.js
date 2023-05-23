import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { useFormik } from 'formik';
import * as yup from 'yup';
// import Cookies from "js-cookie";


function Login({handleLogin}) {
    const navigate = useNavigate();

    const formSchema = yup.object().shape({
        username: yup.string().required('Username is required'),
        password: yup.string().required('Password is required')
    })

    const formik = useFormik({
        initialValues: {
        username: '',
        password: ''
        },
        validationSchema: formSchema,
        onSubmit: (values)=>{
        fetch('/login',{
            method: 'POST',
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify(values, null, 2)
        })
        .then((resp)=>{
            if (resp.status ===200){
            resp.json()
            .then((user)=> handleLogin(user))
            navigate('/recipes')
            }
        })
        }

    })

    return (
        <form onSubmit={formik.handleSubmit}>
        <label htmlFor="username">Username</label>
        <input
            id="username"
            name="username"
            type="text"
            value = {formik.values.username}
            onChange ={formik.handleChange}
            onBlur = {formik.handleBlur}
            />
            {formik.touched.username && formik.errors.username ?(
            <div>{formik.errors.username} </div>) : null}
        <label htmlFor="password">Password</label>
        <input
            id="password"
            name="password"
            type="password"
            value={formik.values.password}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            />
            {formik.touched.password && formik.errors.password ? (
            <div>{formik.errors.password}</div>) : null}
            <button type="submit">Log In</button>
        </form>
    
    )
    }

export default Login;