import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Signup({ setUser }) {
  const [formData, setFormData] = useState({ username: "", password: "", postcode: "" });
  const navigate = useNavigate();

  function handleChange(e) {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    fetch("http://localhost:5000/api/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData)
    })
      .then(res => res.json())
      .then(user => {
        setUser(user);
        navigate("/plans");
      })
      .catch(() => alert("Signup failed"));
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Sign Up</h2>
      <input name="username" placeholder="Username" onChange={handleChange} required />
      <input name="password" type="password" placeholder="Password" onChange={handleChange} required />
      <input name="postcode" placeholder="Postcode" onChange={handleChange} required />
      <button type="submit">Register</button>
    </form>
  );
}

export default Signup;
