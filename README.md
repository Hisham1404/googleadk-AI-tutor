# AI Tutor - Multi-Agent Learning System

<div align="center">

![AI Tutor Logo](https://img.shields.io/badge/AI-Tutor-blue?style=for-the-badge&logo=graduation-cap)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.12-green?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Google AI](https://img.shields.io/badge/Google-AI-red?style=flat&logo=google)](https://ai.google.dev/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)](LICENSE)

**An intelligent tutoring system powered by Google's Gemini AI with specialized multi-agent architecture**

[Features](#features) • [Installation](#installation) • [Configuration](#configuration) • [Usage](#usage) • [API](#api-documentation) • [Contributing](#contributing)

</div>

## 🎯 Overview

AI Tutor is a sophisticated educational platform that leverages Google's Gemini AI through a multi-agent system to provide personalized learning experiences. The system intelligently routes questions to specialized agents based on subject matter, ensuring accurate and contextually relevant responses.

### 🏗️ Architecture

The system uses a **Root Orchestrator** that manages and delegates queries to specialized agents:

- **Root Orchestrator**: Analyzes queries and manages workflow between agents
- **Mathematics Agent**: Handles calculations, algebra, calculus, and mathematical problems
- **Physics Agent**: Covers physics concepts, constants, and physical phenomena
- **Chemistry Agent**: Specializes in elements, compounds, and chemical reactions
- **News Analyst**: Searches and analyzes latest AI news and developments

## ✨ Features

### 🤖 Multi-Agent Intelligence
- **Smart Query Routing**: Automatically determines the best agent for each question
- **Real-time Workflow**: Visual representation of agent thinking process

### 🎨 Modern Frontend
- **Elegant UI**: Beautiful black & white design with smooth animations
- **Agent Dashboard**: Live view of available agents and their capabilities
- **Thinking Panel**: Real-time visualization of agent workflow
- **Responsive Design**: Works seamlessly on desktop and mobile devices

### 📝 Advanced Formatting
- **Markdown Support**: Rich text formatting for better readability
- **Code Highlighting**: Syntax highlighting for code snippets
- **Mathematical Notation**: Proper formatting for equations and formulas

### 🔍 Specialized Tools
- **Calculator**: Advanced mathematical computations
- **Constants Lookup**: Access to physical constants and formulas
- **Elements Database**: Comprehensive chemical element information
- **Web Search**: Real-time AI news and article retrieval

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Google AI API Key ([Get one here](https://aistudio.google.com/app/apikey))
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/aitutor.git
   cd aitutor
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment configuration**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

5. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Google AI API Configuration (Recommended for development)
GOOGLE_AI_API_KEY=your_google_ai_api_key_here

# Alternative: Google Cloud Vertex AI (For production)
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1

# Optional: Application Settings
APP_NAME=aitutor
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

### API Key Setup

#### Option 1: Google AI Studio (Recommended)
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file as `GOOGLE_AI_API_KEY`

#### Option 2: Google Cloud Vertex AI
1. Set up a Google Cloud Project
2. Enable Vertex AI API
3. Configure authentication:
   ```bash
   gcloud auth application-default login
   ```
4. Add project details to `.env` file

## 🎓 Agent Capabilities

### 📊 Mathematics Agent
- **Calculations**: Basic arithmetic to advanced calculus
- **Equation Solving**: Linear, quadratic, and polynomial equations
- **Tools**: Advanced calculator with symbolic computation
- **Examples**: 
  - "Solve: 2x + 5 = 15"
  - "Calculate the derivative of x²"
  - "What is the integral of sin(x)?"

### ⚛️ Physics Agent
- **Concepts**: Mechanics, thermodynamics, electromagnetism
- **Constants**: Physical constants and universal values
- **Tools**: Physics constants lookup database
- **Examples**:
  - "What is the speed of light?"
  - "Explain Newton's second law"
  - "Calculate kinetic energy of a 10kg object at 5m/s"

### 🧪 Chemistry Agent
- **Elements**: Periodic table information and properties
- **Reactions**: Chemical equations and stoichiometry
- **Tools**: Comprehensive elements database
- **Examples**:
  - "Properties of Carbon"
  - "Balance: H2 + O2 → H2O"
  - "What is the atomic mass of Gold?"

### 📰 News Analyst
- **AI News**: Latest developments in artificial intelligence
- **Research**: Current AI research and breakthroughs
- **Tools**: Real-time web search capabilities
- **Examples**:
  - "Latest AI news and developments"
  - "Recent breakthroughs in machine learning"
  - "Current AI industry trends"

## 📱 Usage

### Basic Interaction

1. **Ask Questions**: Type your question in the input field
2. **Watch the Workflow**: Observe the thinking panel for agent routing
3. **Get Answers**: Receive formatted responses with proper markup

### Example Queries

```
Mathematics: "What is the square root of 144?"
Physics: "What is the gravitational constant?"
Chemistry: "What are the properties of Hydrogen?"
News: "What are the latest AI developments?"
Multi-agent: "If light travels at c, how long to reach Alpha Centauri?"
```

### Frontend Features

- **Agent Sidebar**: View all available agents and their status
- **Thinking Panel**: Real-time workflow visualization (collapsible)
- **Example Questions**: Quick-start buttons for testing
- **Markdown Rendering**: Bold, italic, code, and heading support
- **Responsive Design**: Mobile-friendly interface

## 🔌 API Documentation

### Endpoints

#### POST `/api/query`
Process a user query through the multi-agent system.

**Request Body:**
```json
{
  "text": "Your question here"
}
```

**Response:**
```json
{
  "response": "Agent-generated response with markdown formatting"
}
```

#### GET `/`
Serves the main application interface.

#### Static Files `/static/`
- `index.html`: Main application interface
- `style.css`: Styling and animations
- `script.js`: Frontend logic and agent workflow

### Agent Workflow API

The system automatically:
1. Analyzes the input query
2. Determines appropriate agent(s)
3. Routes query to specialist agents
4. Synthesizes final response
5. Returns formatted answer

## 🏃‍♂️ Development

### Project Structure

```
aitutor/
├── main.py                 # FastAPI application and routing
├── multiagent/            # Multi-agent system
│   ├── agent.py          # Root orchestrator agent
│   └── subagents/        # Specialized agents
│       ├── maths/        # Mathematics agent
│       ├── physics/      # Physics agent
│       ├── chemistry/    # Chemistry agent
│       └── ai_news/      # News analyst agent
├── static/               # Frontend assets
│   ├── index.html       # Main UI
│   ├── style.css        # Styling
│   └── script.js        # Frontend logic
├── requirements.txt      # Python dependencies
├── .env                 # Environment configuration
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

### Adding New Agents

1. Create agent directory in `multiagent/subagents/`
2. Implement agent with tools in `agent.py`
3. Add agent to root orchestrator in `multiagent/agent.py`
4. Update frontend agent list in `static/index.html`
5. Add agent styling in `static/style.css`
6. Update workflow detection in `static/script.js`

## 🐛 Troubleshooting

### Common Issues

**API Key Error:**
```
GOOGLE_AI_API_KEY not found
```
*Solution*: Ensure your `.env` file contains a valid Google AI API key.

**Module Import Error:**
```
ModuleNotFoundError: No module named 'multiagent'
```
*Solution*: Run `pip install -r requirements.txt` in your virtual environment.

**Port Already in Use:**
```
Address already in use
```
*Solution*: Use a different port: `uvicorn main:app --port 8001`

**Frontend Not Loading:**
- Check that static files are in the correct directory
- Verify file encoding is UTF-8
- Ensure FastAPI static files mount is configured

### Performance Optimization

- Enable response caching for frequently asked questions
- Implement request rate limiting for production
- Use connection pooling for database operations
- Consider load balancing for high-traffic scenarios

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

### Code Standards

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for new functions and classes
- Include tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google AI](https://ai.google.dev/) for Gemini API
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework
- [Font Awesome](https://fontawesome.com/) for icons
- The open-source community for inspiration and tools

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/aitutor/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/aitutor/discussions)
- **Email**: support@aitutor.com

---

<div align="center">

**Made with ❤️ for education and learning**

[⭐ Star this repo](https://github.com/yourusername/aitutor) • [🐛 Report Bug](https://github.com/yourusername/aitutor/issues) • [💡 Request Feature](https://github.com/yourusername/aitutor/issues)

</div> 