import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { Link, Navigate, useNavigate} from 'react-router-dom'
import Reg from "./Reg.js";
import update from "./update.js";
import Delete from "./delete";
import "./Login.css";

export default function Login(){
    var [email, setEmail] = useState("");
    var [pwd, setPwd] = useState("");
    var [error,setError] = useState('');
    const navigate = useNavigate();
    var [isValid, setIsValid] = useState(false);
    const regex = new RegExp(/^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/);

    function validateEmail(email){
        
        if(regex.test(email)) setIsValid = true;
        else setIsValid = false;
    }

    function handleSubmit(event) {
        event.preventDefault();
        const postBody = {method: 'Post', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({"username": email, "password": pwd})};
        fetch('http://localhost:8999/login', postBody)
        .then(response => response.json()
        .then(data => {
            console.log(data)
            setError(data)
            if(data == "matched") {
                navigate('/home')
            }
            })
        )
    }

    return (
        <div className="Login">
            <h1>Log in</h1>
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
                <Button block size = "lg" type = "submit" disabled={validateEmail(email)}>
                    Login
                </Button>
                <Link to = {'/Reg'}>
                    <Button>
                        Register
                    </Button>
                </Link>
                <Link to = {'/Update'}>
                    <Button>
                        Update Password
                    </Button>
                </Link>
                <Link to = {'/delete'}>
                    <Button>
                        Delete Account
                    </Button>
                </Link>
            </Form>
        </div>
    )
}