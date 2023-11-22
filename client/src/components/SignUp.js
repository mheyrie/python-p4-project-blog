import React, { useEffect, useState } from 'react'
import { useFormik } from "formik";
import * as yup from "yup";

function SignUp() {

  const [users, setUsers] = useState([{}]);
  const [reloadPage, setReloadPage] = useState(false);


  useEffect(() =>{
    fetch('/users')
    .then((res) => res.json())
    .then((data) => {
      setUsers(data);
    });
  }, [reloadPage]);

  const formSchema = yup.object().shape({
    name: yup.string().required("Enter you full names here"),
    email: yup.string().email("Invalid Email").required(),
    phone_number: yup
      .number()
      .integer()
      .required()
      .max(13),
    password: yup.string()
      .required()
      .max(13),
  });

  const formik = useFormik({
    initialValues: {
      name: "",
      email: "",
      phone_number: "",
      password: "",
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch('/users', {
        method: 'POST',
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values, null, 2),
      }).then((res) => {
        if (res.status == 200) {
          setReloadPage(!reloadPage);
        }
      });
    },
  });

  return (
    <div>
      <h1>User Sign up form</h1>
      <form onSubmit={formik.handleSubmit} style={{ margin: "30px" }}>
        <label htmlFor="name">Name: </label>
        <input 
          id="name"
          name="name"
          onChange={formik.handleChange}
          value={formik.values.name}
        />
        <br />

        <label htmlFor="email"> Email Address:  </label>
        <input
          id="email"
          name="email"
          onChange={formik.handleChange}
          value={formik.values.email}
        />
        <br />

        <label htmlFor="phone_number"> Phone Number: </label>
        <input
          id="phone_number"
          name="phone_number"
          onChange={formik.handleChange}
          value={formik.values.phone_number}
        />
         <br />

        <label htmlFor="password"> Password: </label>
        <input
          id="password"
          name="password"
          onChange={formik.handleChange}
          value={formik.values.password}
        />
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  )
}

export default SignUp