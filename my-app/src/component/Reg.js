import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Login from "./Login.js";
import { Link } from 'react-router-dom'
import "./Reg.css";

export default function Reg(){
    var [email, setEmail] = useState("");
    var [pwd, setPwd] = useState("");
    var [isValid, setIsValid] = useState(false);
    const regex = new RegExp(/^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/);

    function validateEmail(email) {
        if(regex.test(email)) setIsValid = true;
        else setIsValid = false;
    }

    function handleSubmit(event) {
        event.preventDefault();
    }

    return (
        <div className = "Reg">
            <h1>Register</h1>
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
                <Link to = {'/Login'}>
                    <Button block size = "lg" type = "submit" disabled={validateEmail(email)}>
                        Register
                    </Button>
                </Link>
                </Form>
        </div>
    )
}