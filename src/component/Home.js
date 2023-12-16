import React, { useState } from "react";
import "./Home.css";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import HomeImg from "../assets/images/shopping.jpg";
import Image from "../assets//images/Home-img.jpg";

const HomePage = () => {
  const [age, setAge] = useState("");
  const [annualIncome, setAnnualIncome] = useState("");
  const [spendScore, setSpendScore] = useState("");
  const [responseData, setResponseData] = useState(null);
  const naviagate = useNavigate();

  const handleAgeChange = (e) => {
    setAge(e.target.value);
  };

  const handleAnnualIncomeChange = (e) => {
    setAnnualIncome(e.target.value);
  };

  const handleSpendScoreChange = (e) => {
    setSpendScore(e.target.value);
  };

  const handleLogout = () => {
    localStorage.removeItem("login");
    naviagate("/");
  };
  const handleGraph = () => {
    naviagate("/customer_segmentation");
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post("http://localhost:5000/process_form", {
        age,
        annualIncome,
        spendScore,
      })
      .then((response) => {
        setResponseData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });

    // Perform form submission logic here
    console.log("Age:", age);
    console.log("Annual Income:", annualIncome);
    console.log("Spend Score:", spendScore);

    // Clear form fields
    setAge("");
    setAnnualIncome("");
    setSpendScore("");
  };

  return (
    <>
      <div className="home-heading">
        <h1> Lovelace</h1>
        <button type="logout" className="logout-button" onClick={handleLogout}>
          Log out
        </button>
      </div>
      <div className="home-container">
        <div className="about">
          <div className="home-image">
            <img src={HomeImg} alt="home-img" />
          </div>
          <h1>Boost Your Bussiness</h1>
          Using hierarchical clustering on shopping mall data, we find patterns
          in customer spend score and demographics. It helps identify customer
          segments, understand similarities, and enable targeted marketing for
          personalized experiences.
        </div>

        <div className="home-form-container">
          <h1>Provide your details</h1>
          <form onSubmit={handleSubmit}>
            <div className="home-form-group">
              <label htmlFor="age" className="home-label">
                Age
              </label>
              <input
                type="number"
                id="age"
                value={age}
                onChange={handleAgeChange}
                required
                placeholder="18-70"
              />
            </div>
            <div className="home-form-group">
              <label htmlFor="annualIncome" className="home-label">
                Annual Income (K$)
              </label>
              <input
                type="number"
                id="annualIncome"
                value={annualIncome}
                onChange={handleAnnualIncomeChange}
                required
                placeholder="15-137"
              />
            </div>
            <div className="home-form-group">
              <label htmlFor="spendScore" className="home-label">
                Spend Score
              </label>
              <input
                type="number"
                id="spendScore"
                value={spendScore}
                onChange={handleSpendScoreChange}
                required
                placeholder="0-100"
              />
            </div>
            <button type="submit" className="submit-button">
              Submit
            </button>
          </form>
        </div>
        <div className="image-back">
          <img src={Image} alt="back" />
          <h3>
            Harness the Power of Customer Clustering
            <br /> to Drive Growth and Engagement
          </h3>
        </div>
      </div>
      {/* <div className="graph"> */}

      {/* </div> */}
      <div className="home-result">
        {responseData ? (
          <div className="home-response">
            <h3>Result</h3>
            {/* <pre>{JSON.stringify(responseData, null, 2)}</pre> */}
            {/* {age !== "" && annualIncome !== "" && spendScore !== "" && (
            )} */}
            <h4>Cluster No. : {responseData.Cluster}</h4>
            <h4>{responseData.labels}</h4>
          </div>
        ) : (
          <p></p>
        )}
      </div>
      <button type="graph" className="graph-button" onClick={handleGraph}>
        Discover More
      </button>
    </>
  );
};

export default HomePage;
