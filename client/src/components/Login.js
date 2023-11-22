import React from 'react';
import { useFormik } from "formik";
import * as yup from "yup";



const schema = yup.object().shape({
    email: yup.string()
        .required("Enter email address")
        .email("Invalid email format"),
    password: yup.string()
        .required("Password is required")
        .min(12, "Password must be least 12 charcters")
});


function Login() {
     
  return (
    <div>Login</div>
  )
}

export default Login