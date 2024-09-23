import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import AgentManagement from './components/AgentManagement';
import Employment from './components/Employment';
import Reporting from './components/Reporting';
import AIChat from './components/AIChat';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/agent-management" component={AgentManagement} />
          <Route path="/employment" component={Employment} />
          <Route path="/reporting" component={Reporting} />
          <Route path="/ai-chat" component={AIChat} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
