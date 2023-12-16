import React from "react";
import {
  BrowserRouter as Router,
  useNavigate,
  Routes,
  Route,
} from "react-router-dom";
import LoginPage from "./component/LoginPage";
import RegistrationPage from "./component/RegistrationPage";
import Graph from "./component/Graph";
import ProtectedRoute from "./component/ProtectedRoute";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<LoginPage />} />
        <Route path="/register" element={<RegistrationPage />} />
        <Route path="/Home" element={<ProtectedRoute />} />
        <Route path="/customer_segmentation" element={<Graph />} />
      </Routes>
    </Router>
  );
};

export default App;
