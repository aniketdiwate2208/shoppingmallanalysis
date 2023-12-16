import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./RegistrationPage.css";
import { registerUser } from "../firebase";
import SignUp from "../assets/images/regist.jpg";

const RegistrationPage = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleNameChange = (e) => {
    setName(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleRegistration = (e) => {
    e.preventDefault();
    // Perform registration logic here
    console.log("Name:", name);
    console.log("Email:", email);
    // console.log("Password:", password);

    //firebase
    registerUser(email, password, name);
    // Clear form fields
    setName("");
    setEmail("");
    setPassword("");
    navigate("/");
  };

  return (
    <>
      <div className="title-reg">
        <p>Boost Your Sales with Customer Segmentation</p>
      </div>
      <div className="registration-container">
        <div className="registration-content">
          <h1 className="registration-title">Registration Page</h1>
          <form onSubmit={handleRegistration}>
            <div className="registration-row">
              <div className="registration-input-group">
                <label htmlFor="name" className="regi-label">
                  Name
                </label>
                <input
                  type="text"
                  id="name"
                  value={name}
                  onChange={handleNameChange}
                  required
                  placeholder="Name"
                />
              </div>
            </div>
            <div className="registration-row">
              <div className="registration-input-group">
                <label htmlFor="email" className="regi-label">
                  Email
                </label>
                <input
                  type="email"
                  id="email"
                  value={email}
                  onChange={handleEmailChange}
                  required
                  placeholder="name@example.com"
                />
              </div>
            </div>
            <div className="registration-row">
              <div className="registration-input-group">
                <label htmlFor="password" className="regi-label">
                  Password
                </label>
                <input
                  type="password"
                  id="password"
                  value={password}
                  onChange={handlePasswordChange}
                  required
                  placeholder="Password"
                />
              </div>
            </div>
            <div className="registration-row">
              <button type="submit" className="registration-button">
                Register
              </button>
            </div>
          </form>
        </div>
        <div className="registration-image-container">
          <img src={SignUp} alt="Registration" />
        </div>
      </div>
    </>
  );
};

export default RegistrationPage;
