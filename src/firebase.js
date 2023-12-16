import firebase from "firebase/compat/app";
import "firebase/compat/auth";
import "firebase/compat/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyCV5agkRZu4T9PZAh7ZFB_AKuSvkxJbLDY",
  authDomain: "lovelace-ef736.firebaseapp.com",
  projectId: "lovelace-ef736",
  storageBucket: "lovelace-ef736.appspot.com",
  messagingSenderId: "262210385846",
  appId: "1:262210385846:web:15cabb53e9d81ab8f93317",
  measurementId: "G-Z7LRYEC8DG",
};

firebase.initializeApp(firebaseConfig);

export const auth = firebase.auth();
export const firestore = firebase.firestore();

export const registerUser = async (email, password, username) => {
  try {
    const { user } = await auth.createUserWithEmailAndPassword(email, password);
    await firestore.collection("users").doc(user.uid).set({ username });
    console.log("User registered successfully!");
  } catch (error) {
    console.error("Error registering user:", error);
    alert("Email id is already taken");
  }
};
