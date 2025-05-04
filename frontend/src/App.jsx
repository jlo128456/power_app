import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Signup from "./components/Signup";
import PlanFinder from "./components/PlanFinder";
import Home from "./components/Home";
function App() {
  const [user, setUser] = useState(null);

  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} /> {/* Home page */}
        {/* <Route path="/" element={<Signup setUser={setUser} />} />  */}
        <Route path="/plans" element={<PlanFinder />} />
      </Routes>
    </div>
  );
}

export default App;
