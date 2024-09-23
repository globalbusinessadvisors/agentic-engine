import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Bar, Line, Pie } from 'react-chartjs-2';

const Reporting = () => {
  const [reportData, setReportData] = useState([]);
  const [chartType, setChartType] = useState('bar');

  useEffect(() => {
    fetchReportData();
  }, []);

  const fetchReportData = async () => {
    try {
      const response = await axios.get('http://localhost:8000/reports');
      setReportData(response.data);
    } catch (error) {
      console.error('Error fetching report data:', error);
    }
  };

  const handleChartTypeChange = (e) => {
    setChartType(e.target.value);
  };

  const chartData = {
    labels: reportData.map((data) => data.label),
    datasets: [
      {
        label: 'Report Data',
        data: reportData.map((data) => data.value),
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
      },
    ],
  };

  return (
    <div>
      <h1>Reporting</h1>
      <div>
        <label htmlFor="chartType">Select Chart Type: </label>
        <select id="chartType" value={chartType} onChange={handleChartTypeChange}>
          <option value="bar">Bar</option>
          <option value="line">Line</option>
          <option value="pie">Pie</option>
        </select>
      </div>
      <div>
        {chartType === 'bar' && <Bar data={chartData} />}
        {chartType === 'line' && <Line data={chartData} />}
        {chartType === 'pie' && <Pie data={chartData} />}
      </div>
      <table>
        <thead>
          <tr>
            <th>Label</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {reportData.map((data) => (
            <tr key={data.id}>
              <td>{data.label}</td>
              <td>{data.value}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Reporting;
