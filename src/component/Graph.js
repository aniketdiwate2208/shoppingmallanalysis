import React, { useState } from "react";
import { v4 as uuidv4 } from "uuid";
import "./Graph.css";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import Image1 from "../assets/images/graph1.jpg";
import Image2 from "../assets/images/graph2.jpg";

const GraphPage = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [imageData, setImageData] = useState(null);
  const [anotherImageData, setAnotherImageData] = useState(null);
  const [responseData, setResponseData] = useState(null);
  const naviagate = useNavigate();

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleLogout = () => {
    localStorage.removeItem("login");
    naviagate("/");
  };

  const handleUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append("file", selectedFile);

      await axios
        .post("http://localhost:5000/upload", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          // Handle successful upload response
          console.log("Upload successful:", response.data);
          setResponseData(response.data);
          fetchImage();
        })
        .catch((error) => {
          // Handle upload error
          console.error("Upload error:", error);
        });
    } else {
      console.log("No file selected");
    }
  };

  const fetchImage = async () => {
    try {
      const response = await axios.get("http://localhost:5000/image_link", {
        responseType: "arraybuffer",
      });
      const base64Image = btoa(
        new Uint8Array(response.data).reduce(
          (data, byte) => data + String.fromCharCode(byte),
          ""
        )
      );
      const imageDataUrl = `data:image/jpeg;base64,${base64Image}`;
      setImageData(imageDataUrl);

      const anotherResponse = await axios.get(
        "http://localhost:5000/scatter_plot",
        {
          responseType: "arraybuffer",
        }
      );
      const anotherBase64Image = btoa(
        new Uint8Array(anotherResponse.data).reduce(
          (data, byte) => data + String.fromCharCode(byte),
          ""
        )
      );
      const anotherImageDataUrl = `data:image/jpeg;base64,${anotherBase64Image}`;
      setAnotherImageData(anotherImageDataUrl);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <>
      <div className="home-heading">
        <h1>Lovelace</h1>
        <button type="logout" className="logout-button" onClick={handleLogout}>
          Log out
        </button>
      </div>
      <div className="Home">
        <div className="image1">
          <img src={Image1} alt="home" />
        </div>
        <div className="instruction-component">
          <h1>
            Shopping Mall Customer <br />
            Segmentation
          </h1>
          <ul>
            <li>Upload your csv file</li>
            <li>
              Make sure that your csv file conatain (Age, Annual Income,
              Spending Score) column in it
            </li>
          </ul>
        </div>
        <div className="image2">
          <img src={Image2} alt="home" />
        </div>
      </div>
      <div className="file-uploader">
        <input type="file" className="file-input" onChange={handleFileChange} />
        <button className="upload-button" onClick={handleUpload}>
          Upload
        </button>
      </div>
      <div className="graph-component">
        <div className="graphs">
          <div className="pie-chart">
            {imageData ? <img src={imageData} alt="Loaded" /> : <p></p>}
          </div>
          <div className="scattered-graph">
            {anotherImageData ? (
              <img src={anotherImageData} alt="Loaded" />
            ) : (
              <p></p>
            )}
          </div>
        </div>
        <div className="Result">
          {responseData ? (
            <div className="Response">
              <h1>Statistical Analysis</h1>
              {Object.entries(responseData).map(([key, value]) => {
                return (
                  <div className="cluster" key={uuidv4()}>
                    <table>
                      <thead>
                        <tr>
                          <th>Cluster</th>
                          <th>Average Age</th>
                          <th>Average Annual Income (K$)</th>
                          <th>Annual Income Range (K$)</th>
                          <th>Spending Score Range</th>
                          <th>Average Spending Score</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>{key}</td>
                          <td>{value["Average Age"]}</td>
                          <td>{value["Average Annual Income(K$)"]}</td>
                          <td>
                            {value["Minimum Annual Income (K$)"]} -{" "}
                            {value["Maximum Annual Income (K$)"]}
                          </td>
                          <td>
                            {value["Minimum Spending Score"]} -{" "}
                            {value["Maximum Spending Score"]}
                          </td>
                          <td>{value["Spending Score (1-100)"]}</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                );
              })}
              {/* <pre>{JSON.stringify(responseData, null, 2)}</pre> */}
              {/* <h3>Average Age : {responseData["cluster 0"]["Average Age"]}</h3> */}
            </div>
          ) : (
            <p></p>
          )}
        </div>
      </div>
    </>
  );
};

export default GraphPage;
