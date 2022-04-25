import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Login from "./Login.js";
import { Link } from 'react-router-dom'
import "./Reg.css";

export default function Reg(){
    var [email, setEmail] = useState("");
    var [pwd, setPwd] = useState("");
    var [newpwd, setNewPwd] = useState("");
    var [error,setError] = useState('');
    var [isValid, setIsValid] = useState(false);
    const regex = new RegExp(/^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/);

    function validateEmail(email) {
        if(regex.test(email)) setIsValid = true;
        else setIsValid = false;
    }

    function handleSubmit(event) {
        event.preventDefault();
        console.log("hello")
        const postBody = {method: 'Post', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({"username": email, "password": pwd, "newPassword": newpwd})};
        fetch('http://localhost:8999/update', postBody)
        .then(response => response.json()
        .then(data => {
            console.log(data)
            setError(data)
            })
        )
    }

    return (
        <div className="register">
            <h1>Update</h1>
            <Form onSubmit = {handleSubmit}>
                <Form.Group size = "lg" controlId = "email">
                    <Form.Label>Email</Form.Label>
                    <Form.Control
                        autoFocus
                        type = "email"
                        value = {email}
                        onChange = {(e) => setEmail(e.target.value)}
                    />
                </Form.Group>

                <Form.Group size = "lg" controlId = "pwd">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                        autoFocus
                        type = "pwd"
                        value = {pwd}
                        onChange = {(e) => setPwd(e.target.value)}
                    />
                </Form.Group>
                
                <Form.Group size = "lg" controlId = "newpwd">
                    <Form.Label>ew Password</Form.Label>
                    <Form.Control
                        autoFocus
                        type = "newpwd"
                        value = {newpwd}
                        onChange = {(e) => setNewPwd(e.target.value)}
                    />
                </Form.Group>

                <Link to = {'/Login'} >
                    <Button>
                    Login page
                    </Button>
                </Link>

                <div className="hello">
                    <Button block size = "lg" type = "submit" disabled={validateEmail(email)}>
                        Update Password
                    </Button>
                {<h3 className="error"> {error} </h3> }
                </div>
                
                
            </Form>

        </div>
    )
}