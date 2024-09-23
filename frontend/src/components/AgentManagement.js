import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AgentManagement = () => {
  const [agents, setAgents] = useState([]);
  const [newAgent, setNewAgent] = useState({ name: '', role: '' });

  useEffect(() => {
    fetchAgents();
  }, []);

  const fetchAgents = async () => {
    try {
      const response = await axios.get('http://localhost:8000/agents');
      setAgents(response.data);
    } catch (error) {
      console.error('Error fetching agents:', error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewAgent({ ...newAgent, [name]: value });
  };

  const handleAddAgent = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/agents', newAgent);
      fetchAgents();
      setNewAgent({ name: '', role: '' });
    } catch (error) {
      console.error('Error adding agent:', error);
    }
  };

  return (
    <div>
      <h1>Agent Management</h1>
      <form onSubmit={handleAddAgent}>
        <input
          type="text"
          name="name"
          value={newAgent.name}
          onChange={handleInputChange}
          placeholder="Agent Name"
          required
        />
        <input
          type="text"
          name="role"
          value={newAgent.role}
          onChange={handleInputChange}
          placeholder="Agent Role"
          required
        />
        <button type="submit">Add Agent</button>
      </form>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Role</th>
          </tr>
        </thead>
        <tbody>
          {agents.map((agent) => (
            <tr key={agent.id}>
              <td>{agent.name}</td>
              <td>{agent.role}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AgentManagement;
