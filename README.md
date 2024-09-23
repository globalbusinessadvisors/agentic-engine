# Agentic Engine

Welcome to the **Agentic Engine**, an integrated platform that brings together agile agent management, employment solutions, reporting tools, and advanced AI interactions. This engine consolidates multiple repositories to deliver a comprehensive solution for modern business needs.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Agentic Engine** is a unified system that integrates the functionalities of several repositories to empower businesses with agent-based solutions:

- **Agile Agents**: Manage and deploy agile agents effectively.
- **Agentic Employment**: Solutions for modern, flexible employment models.
- **Reporting Tools**: Generate insightful reports for data-driven decisions.
- **AI Interactions**: Leverage AI models for enhanced user experiences.
- **Backend Services**: Robust APIs and database management.
- **Automation**: Streamline tasks with automation tools.

## Features

- **Agile Agent Management**: Utilize tools from [`agileagents`](https://github.com/globalbusinessadvisors/agileagents) to oversee agent activities.
- **Agentic Employment Solutions**: Implement modern employment models from [`agentic-employment`](https://github.com/globalbusinessadvisors/agentic-employment).
- **Data Development**: Employ [`rUv-dev`](https://github.com/globalbusinessadvisors/rUv-dev) for data handling and processing.
- **Comprehensive Reporting**: Generate detailed reports using [`agentic-reports`](https://github.com/globalbusinessadvisors/agentic-reports).
- **Business Analytics and Machine Learning**: Integrate models from [`baml`](https://github.com/globalbusinessadvisors/baml) for pydantic predictive analytics.
- **AI-Powered User Interface**: Create interactive AI experiences with [`hugging-chat-ui`](https://github.com/globalbusinessadvisors/hugging-chat-ui).
- **Scalable Database Management**: Use [`supabase`](https://github.com/globalbusinessadvisors/supabase) for efficient database solutions.
- **Automation and Testing**: Automate tasks and testing with [`selenium`](https://github.com/globalbusinessadvisors/selenium).
- **Fast API Development**: Build high-performance APIs using [`fastapi`](https://github.com/globalbusinessadvisors/fastapi).
- **AI Integration**: Connect to OpenAI's services with [`openai-python`](https://github.com/globalbusinessadvisors/openai-python).

## Architecture

The Agentic Engine is built with modularity and scalability in mind, combining various technologies:

- **Frontend**: Interactive interfaces developed with `hugging-chat-ui`.
- **Backend**: APIs and services built using `fastapi`.
- **Database**: Managed by `supabase` for real-time data handling.
- **Automation**: Task automation and browser interactions via `selenium`.
- **AI Models**: Integrated through `openai-python` and `baml` for intelligent features.

## Getting Started

Follow these steps to set up the Agentic Engine locally.

### Prerequisites

- **Python**: Version 3.8 or higher.
- **Node.js and npm**: For frontend development.
- **Docker**: Optional, for containerization.
- **PostgreSQL**: If not using Docker, ensure PostgreSQL is installed for `supabase`.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/globalbusinessadvisors/agentic-engine.git
   cd agentic-engine
   ```

2. **Install Backend Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Frontend Dependencies**

   ```bash
   cd frontend
   npm install
   cd ..
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add the necessary configurations:

   ```ini
   DATABASE_URL=your_database_url
   SECRET_KEY=your_secret_key
   OPENAI_API_KEY=your_openai_api_key
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   ```

5. **Run Database Migrations**

   Apply migrations to set up your database schema:

   ```bash
   alembic upgrade head
   ```

6. **Start the Backend Server**

   ```bash
   uvicorn main:app --reload
   ```

7. **Start the Frontend Server**

   ```bash
   cd frontend
   npm start
   ```

## Usage

- **Access the Frontend**: Navigate to `http://localhost:3000` in your web browser.
- **API Documentation**: Visit `http://localhost:8000/docs` for interactive API docs powered by Swagger UI.
- **AI Interaction**: Utilize the AI chat interface for enhanced user experiences.
- **Agent Management**: Oversee and manage agents through the provided dashboards.
- **Reporting**: Generate and view reports to gain insights into your data.

## Contributing

We welcome contributions to the Agentic Engine! To contribute:

1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page.
2. **Create a New Branch**: For your feature or bug fix.

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**: Implement your feature or fix.
4. **Commit Your Changes**: Write clear and concise commit messages.

   ```bash
   git commit -m "Add new feature XYZ"
   ```

5. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Submit a Pull Request**: Go to the original repository and create a pull request from your fork.

## License

The Agentic Engine is licensed under the [MIT License](LICENSE).

---

**Note**: Ensure all submodules and dependencies from the original repositories are correctly configured in the Agentic Engine. Check each repository's documentation for specific setup instructions that may be required.

## Backend Folder Structure

The backend folder contains the FastAPI application and related files. The structure is as follows:

```
backend/
├── alembic/
│   ├── versions/
│   │   └── initial_migration.py
│   └── alembic.ini
├── routers/
│   ├── agents.py
│   ├── employment.py
│   ├── reports.py
│   └── ai.py
├── main.py
├── models.py
├── database.py
├── requirements.txt
└── .env
```

## Backend Endpoints

Here are some examples of backend endpoints and their usage:

### Agent Management

- **Create Agent**

  ```http
  POST /agents
  ```

  Request Body:

  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **Get Agents**

  ```http
  GET /agents
  ```

- **Update Agent**

  ```http
  PUT /agents/{agent_id}
  ```

  Request Body:

  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **Delete Agent**

  ```http
  DELETE /agents/{agent_id}
  ```

### Employment Management

- **Create Employment Record**

  ```http
  POST /employment
  ```

  Request Body:

  ```json
  {
    "agent_id": 1,
    "position": "Software Engineer",
    "start_date": "2022-01-01",
    "end_date": "2022-12-31"
  }
  ```

- **Get Employment Records**

  ```http
  GET /employment
  ```

- **Update Employment Record**

  ```http
  PUT /employment/{employment_id}
  ```

  Request Body:

  ```json
  {
    "agent_id": 1,
    "position": "Senior Software Engineer",
    "start_date": "2022-01-01",
    "end_date": "2022-12-31"
  }
  ```

- **Delete Employment Record**

  ```http
  DELETE /employment/{employment_id}
  ```

### Reporting

- **Create Report**

  ```http
  POST /reports
  ```

  Request Body:

  ```json
  {
    "agent_id": 1,
    "report_data": "Report content here"
  }
  ```

- **Get Reports**

  ```http
  GET /reports
  ```

- **Update Report**

  ```http
  PUT /reports/{report_id}
  ```

  Request Body:

  ```json
  {
    "agent_id": 1,
    "report_data": "Updated report content here"
  }
  ```

- **Delete Report**

  ```http
  DELETE /reports/{report_id}
  ```

### AI Interactions

- **Generate AI Response**

  ```http
  POST /ai/generate
  ```

  Request Body:

  ```json
  {
    "prompt": "Hello, how can I help you today?"
  }
  ```

  Response:

  ```json
  {
    "response": "Hi! How can I assist you today?"
  }
  ```
