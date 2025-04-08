import React, { useState, useEffect } from "react";
import axios from "axios";

const MortgageDashboard = () => {
  const [formData, setFormData] = useState({
    applicant_name: "",
    income: "",
    loan_amount: "",
    duration_years: "",
  });
  const [mortgages, setMortgages] = useState([]);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const fetchMortgages = async () => {
    try {
      const res = await axios.get("http://localhost:5000/mortgages");
      setMortgages(res.data);
    } catch (err) {
      setError("Failed to fetch mortgages");
    }
  };

  useEffect(() => {
    fetchMortgages();
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setMessage("");

    const { applicant_name, income, loan_amount, duration_years } = formData;
    if (!applicant_name || !income || !loan_amount || !duration_years) {
      setError("All fields are required");
      return;
    }

    try {
      const res = await axios.post("http://localhost:5000/mortgages", formData);
      setMessage(res.data.message + " | Rating: " + res.data.rating);
      setFormData({
        applicant_name: "",
        income: "",
        loan_amount: "",
        duration_years: "",
      });
      fetchMortgages();
    } catch (err) {
      setError(err.response?.data?.error || "Something went wrong");
    }
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4">Mortgage Application</h2>
      {message && <div className="alert alert-success">{message}</div>}
      {error && <div className="alert alert-danger">{error}</div>}
      <form onSubmit={handleSubmit} className="mb-4">
        <div className="mb-3">
          <label className="form-label">Applicant Name</label>
          <input
            type="text"
            className="form-control"
            name="applicant_name"
            value={formData.applicant_name}
            onChange={handleChange}
            placeholder="Enter name"
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Income</label>
          <input
            type="number"
            className="form-control"
            name="income"
            value={formData.income}
            onChange={handleChange}
            placeholder="Enter income"
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Loan Amount</label>
          <input
            type="number"
            className="form-control"
            name="loan_amount"
            value={formData.loan_amount}
            onChange={handleChange}
            placeholder="Enter loan amount"
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Duration (years)</label>
          <input
            type="number"
            className="form-control"
            name="duration_years"
            value={formData.duration_years}
            onChange={handleChange}
            placeholder="Enter duration"
          />
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>

      <h3>Submitted Mortgages</h3>
      <table className="table table-bordered mt-3">
        <thead>
          <tr>
            <th>Name</th>
            <th>Income</th>
            <th>Loan Amount</th>
            <th>Duration (Years)</th>
            <th>Credit Rating</th>
          </tr>
        </thead>
        <tbody>
          {mortgages.map((m) => (
            <tr key={m.id}>
              <td>{m.applicant_name}</td>
              <td>{m.income}</td>
              <td>{m.loan_amount}</td>
              <td>{m.duration_years}</td>
              <td>{m.credit_rating}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MortgageDashboard;
