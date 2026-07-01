import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import axios from 'axios';

const API_BASE_URL = "http://127.0.0.1:8000";

const FinancialTwinDashboard: React.FC = () => {
  const [loanEligibility, setLoanEligibility] = useState<number>(0);
  const [fraudRisk, setFraudRisk] = useState<string>("low");
  const [scenarioImpact, setScenarioImpact] = useState<any>(null);
  const [query, setQuery] = useState<string>("");
  const [queryResponse, setQueryResponse] = useState<string>("");

  // Sample data for visualization
  const cashFlowData = {
    x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    y: [50000, 45000, 60000, 55000, 70000, 65000],
    type: 'scatter',
    mode: 'lines+markers',
    name: 'Monthly Cash Flow',
    line: { color: '#3b82f6' },
  };

  const fraudRiskData = {
    values: [70, 20, 10],
    labels: ['Low Risk', 'Medium Risk', 'High Risk'],
    type: 'pie',
    marker: {
      colors: ['#10b981', '#f59e0b', '#ef4444'],
    },
  };

  const loanEligibilityData = {
    x: ['Credit Score', 'Income Stability', 'Debt-to-Income'],
    y: [85, 90, 70],
    type: 'bar',
    marker: { color: '#8b5cf6' },
  };

  // --- API Functions ---
  async function fetchLoanEligibility() {
    try {
      const response = await axios.post(`${API_BASE_URL}/predict/loan_eligibility`, {
        user_id: "mock_user_123",
        loan_amount: 500000
      });
      setLoanEligibility(response.data.score);
    } catch (error) {
      console.error("Error fetching loan eligibility:", error);
    }
  }

  async function fetchFraudRisk() {
    try {
      const response = await axios.post(`${API_BASE_URL}/predict/fraud_risk`, {
        user_id: "mock_user_123",
        transaction_id: "mock_tx_456"
      });
      setFraudRisk(response.data.risk);
    } catch (error) {
      console.error("Error fetching fraud risk:", error);
    }
  }

  async function handleQuery() {
    try {
      const response = await axios.post(`${API_BASE_URL}/query`, {
        user_id: "mock_user_123",
        query: query
      });
      setQueryResponse(response.data.response);
      setScenarioImpact(response.data.impact);
    } catch (error) {
      console.error("Error simulating scenario:", error);
      setQueryResponse("Failed to simulate scenario. Please try again.");
    }
  }

  // --- Lifecycle ---
  useEffect(() => {
    fetchLoanEligibility();
    fetchFraudRisk();
  }, []);

  return (
    <div className="p-6 bg-light dark:bg-dark rounded-lg shadow-md">
      <h1 className="text-2xl font-bold mb-6 text-primary">Smart Financial Twin</h1>

      {/* Financial Health Score */}
      <div className="mb-8">
        <h2 className="text-xl font-semibold mb-2">Financial Health Score</h2>
        <div className="bg-white dark:bg-slate-800 p-4 rounded-lg">
          <p className="text-3xl font-bold text-secondary">{loanEligibility * 100}/100</p>
        </div>
      </div>

      {/* Fraud Risk */}
      <div className="mb-8">
        <h2 className="text-xl font-semibold mb-2">Fraud Risk Assessment</h2>
        <div className="bg-white dark:bg-slate-800 p-4 rounded-lg">
          <p className={`text-2xl font-bold ${fraudRisk === "high" ? "text-red-500" : fraudRisk === "medium" ? "text-yellow-500" : "text-green-500"}`}>
            {fraudRisk.toUpperCase()}
          </p>
        </div>
      </div>

      {/* Cash Flow Forecast */}
      <div className="mb-8">
        <h2 className="text-xl font-semibold mb-2">Cash Flow Forecast</h2>
        <Plot
          data={[cashFlowData]}
          layout={{ width: 600, height: 300, title: 'Monthly Cash Flow' }}
          className="w-full"
        />
      </div>

      {/* Fraud Risk Distribution */}
      <div className="mb-8">
        <h2 className="text-xl font-semibold mb-2">Fraud Risk Distribution</h2>
        <Plot
          data={[fraudRiskData]}
          layout={{ width: 400, height: 300, title: 'Fraud Risk Distribution' }}
          className="w-full"
        />
      </div>

      {/* Loan Eligibility */}
      <div className="mb-8">
        <h2 className="text-xl font-semibold mb-2">Loan Eligibility Factors</h2>
        <Plot
          data={[loanEligibilityData]}
          layout={{ width: 500, height: 300, title: 'Loan Eligibility Metrics' }}
          className="w-full"
        />
      </div>

      {/* Simulation Input */}
      <div className="mt-8">
        <h2 className="text-xl font-semibold mb-4">Financial Scenario Simulator</h2>
        <div className="flex gap-4 mb-4">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="What if I buy a ₹15 lakh car?"
            className="flex-1 p-2 border rounded-lg dark:bg-slate-700 dark:border-slate-600"
          />
          <button
            onClick={handleQuery}
            className="bg-primary text-white px-4 py-2 rounded-lg hover:bg-blue-600"
          >
            Simulate
          </button>
        </div>
        {queryResponse && (
          <div className="bg-white dark:bg-slate-800 p-4 rounded-lg mt-4">
            <p className="text-sm">{queryResponse}</p>
            {scenarioImpact && (
              <div className="mt-4">
                <h3 className="font-semibold">Impact:</h3>
                <p>Savings: ₹{scenarioImpact.savings_impact.toLocaleString()}</p>
                <p>Retirement Delay: {scenarioImpact.retirement_delay} years</p>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default FinancialTwinDashboard;