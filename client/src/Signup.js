import React from "react";
import { useNavigate } from 'react-router-dom';
import { useFormik } from "formik";
// import {Formik, Field, Form, ErrorMessage} from "formik";
import * as yup from 'yup'; 
// import {Grid, Paper, Button} from '@material-ui/core';
// import {TextField} from '@material-ui/core';



function SignUp(){
    const navigate = useNavigate()

    const formSchema = yup.object().shape({
        username: Yup.string().min(3, "Its too short").required("Must enter username"),
        email: Yup.string().email("Enter valid email").required("Must enter email"),
        password: Yup.string().min(6, "Minium characters should be 6").required("Must enter password"),
        confirmPassword: Yup.string().oneOf([Yup.ref("password")],"Password not matching").required('Required')
    })
    const formik = useFormik({
        initialValues:{
            email: '',
            username: '',
            password: ''
        },
        validationSchema: formSchema,
        onSubmit: (values)=>{
            fetch('/users', {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
            body: JSON.stringify(values, null, 2),
            }).then((resp)=>{
                if (resp.status === 201){
                    navigate('/login')
                }
            })
        }
    })
    return (
        <form onSubmit= {formik.handleSubmit}>
            <label htmlFor="email">Email Address</label>
            <input
                id = "email"
                name = "email"
                type = "email"
                {...formik.getFieldProps('email')}
            />
            {formik.touched.email && formik.errors.email ?(
                <div>{formik.errors.email} </div>) : null}
            <label htmlFor="username">Username</label>
            <input
                id = "username"
                name = "username"
                type = "text"
                {...formik.getFieldProps('username')}
            />
            {formik.touched.username && formik.errors.username ?(
                <div>{formik.errors.username} </div>) : null}
            <label htmlFor="name">Password</label>
            <input
                id = "password"
                name = "password"
                type = "text"
                {...formik.getFieldProps('password')}
            />
        </form>
    )
}
export default SignUp;

