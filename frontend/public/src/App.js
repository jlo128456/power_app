import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Signup from "./components/Signup";
import PlanFinder from "./components/PlanFinder";

function App() {
  const [user, setUser] = useState(null);

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Signup setUser={setUser} />} />
          <Route path="/plans" element={<PlanFinder />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;