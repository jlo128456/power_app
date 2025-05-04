import React, { useState } from "react";

function PlanFinder() {
  const [postcode, setPostcode] = useState("");
  const [plans, setPlans] = useState([]);

  function handleSearch() {
    fetch(`http://localhost:5000/api/energy-plans-by-postcode/${postcode}`)
      .then(res => res.json())
      .then(data => {
        if (data.error) {
          alert(data.error);
          setPlans([]);
        } else {
          setPlans(data);
        }
      });
  }

  return (
    <div>
      <h2>Find Energy Plans</h2>
      <input
        type="text"
        value={postcode}
        onChange={e => setPostcode(e.target.value)}
        placeholder="Enter postcode"
      />
      <button onClick={handleSearch}>Search</button>

      {plans.length > 0 && (
        <ul>
          {plans.map(plan => (
            <li key={plan.id}>{plan.plan_name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default PlanFinder;
