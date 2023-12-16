import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./LoginPage.css";
import { auth } from "../firebase";
import LoginImage from "../assets/images/login.jpg";

const LoginPage = () => {
  localStorage.removeItem("login");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      await auth.signInWithEmailAndPassword(email, password).then(() => {
        localStorage.setItem("login", true);
        console.log("User logged in:", auth.currentUser.email);
      });
      // User successfully logged in
      // Clear form fields
      setEmail("");
      setPassword("");
      // Redirect to a different page after successful login
      navigate("/Home");
    } catch (error) {
      // Handle login error
      alert("Wrong Credential");
      console.error("Login error:", error);
    }
  };

  return (
    <>
      <div className="title">
        <h2>
          Elevate Your Sales with Lovelace <br /> Your Champion Companion in
          Clustering Excellence!
        </h2>
      </div>
      <div className="container-form">
        <div className="login-image">
          <img src={LoginImage} alt="Login" />
        </div>
        <div className="login-content">
          <form onSubmit={handleLogin}>
            <h2 className="form-title">Sign In</h2>
            <div className="form-group">
              <label htmlFor="email" className="login-label">
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
            <div className="form-group">
              <label htmlFor="password" className="login-label">
                Password
              </label>
              <input
                type="password"
                id="password"
                value={password}
                onChange={handlePasswordChange}
                required
                placeholder="password"
              />
            </div>
            <div className="form-group">
              <button type="login">Log In</button>
            </div>
            <p>
              Don't have an account? <Link to="/register">Register</Link>
            </p>
          </form>
        </div>
      </div>
    </>
  );
};

export default LoginPage;
