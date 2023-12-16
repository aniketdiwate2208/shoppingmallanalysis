import React from "react";
import { Navigate, Route } from "react-router-dom";
import HomePage from "./Home";

const ProtectedRoute = () => {
  const isLogin = localStorage.getItem("login");
  if (isLogin) {
    return <HomePage />;
  } else {
    return <Navigate to="/" />;
  }
};

export default ProtectedRoute;
