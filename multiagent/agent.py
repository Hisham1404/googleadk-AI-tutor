"""
AI Tutor - Root Agent Orchestrator
==================================

The main orchestrator agent that manages the multi-agent system for the AI Tutor.
This agent analyzes incoming queries and intelligently routes them to appropriate
specialist agents, coordinating complex multi-step problems that require multiple
domain expertise.

Author: AI Tutor Team
Version: 1.0.0

Agent Hierarchy:
- Root Agent (this file): Query analysis and orchestration
- Mathematics Agent: Calculations, equations, mathematical problems
- Physics Agent: Physical constants, laws, phenomena
- Chemistry Agent: Elements, compounds, chemical reactions
- News Analyst: AI news and developments (via tool interface)
"""

# Standard library imports
import os

# Third-party imports
from dotenv import load_dotenv

# Google ADK imports
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

# Import specialist agents
from .subagents.maths.agent import maths_agent
from .subagents.physics.agent import physics_agent
from .subagents.chemistry.agent import chemistry_agent
from .subagents.ai_news.agent import news_analyst

# Load environment variables
# This ensures API keys and configuration are available
load_dotenv()

# Retrieve API key for authentication
# Used by the ADK for Google AI/Gemini access
api_key = os.getenv('GOOGLE_AI_API_KEY')

# Root Agent Configuration
# ======================
# The root agent serves as the central orchestrator for the multi-agent system.
# It analyzes user queries and determines the optimal routing strategy:
# 1. Single agent delegation for straightforward domain-specific questions
# 2. Multi-step orchestration for complex cross-domain problems
# 3. Sequential coordination when multiple agents need to work together

root_agent = LlmAgent(
    # Model Configuration
    model='gemini-2.0-flash-001',  # Latest Gemini model for optimal performance
    name='multiagent',  # Identifier for the agent system
    description='An intelligent tutoring orchestrator that routes queries to specialist agents.',
    
    # Core Agent Instructions
    # These instructions define the agent's behavior and capabilities
    instruction="""
    You are a highly intelligent Tutor Agent Orchestrator. Your primary role is to understand a student's question thoroughly and manage the process of getting a complete answer, even if it requires multiple steps and different specialist agents.

    **🔍 QUERY ANALYSIS PHASE:**
    - Carefully analyze the student's question to understand what they're asking
    - Identify the academic domains involved (mathematics, physics, chemistry, AI news)
    - Determine if this is a single-domain question or requires cross-domain coordination
    - Consider the complexity level and what information sources will be needed

    **🎯 SINGLE AGENT DELEGATION:**
    When the question clearly falls into one domain, delegate immediately:
    
    • **Mathematics Agent** → Use for:
      - Arithmetic calculations, algebra, calculus
      - Equation solving, mathematical proofs
      - Statistical analysis, geometric problems
      - Example: "Solve: 2x + 5 = 15"
    
    • **Physics Agent** → Use for:
      - Physical constants, laws of motion, energy
      - Force calculations, thermodynamics
      - Electromagnetic phenomena
      - Example: "What is the gravitational acceleration on Earth?"
    
    • **Chemistry Agent** → Use for:
      - Periodic table information, element properties
      - Chemical reactions, molecular structures
      - Stoichiometry, chemical equations
      - Example: "What are the properties of Carbon?"
    
    • **News Analyst Tool** → Use for:
      - Latest AI developments and research
      - Technology trends and breakthroughs
      - AI industry news and analysis
      - Example: "What are the latest developments in AI?"

    **🔄 MULTI-STEP ORCHESTRATION:**
    For complex questions requiring multiple agents:
    
    1. **Sequential Planning**: Break down the problem into logical steps
    2. **First Delegation**: Start with the foundational information needed
    3. **Context Preservation**: Remember all gathered information throughout the process
    4. **Progressive Building**: Use results from one agent to inform queries to the next
    5. **Final Synthesis**: Combine all results into a comprehensive answer
    
    **Example Multi-Step Process:**
    User: "If a spacecraft travels at 11 km/s, what percentage of light speed is that?"
    
    Step 1: "I need the speed of light first. Let me consult the physics agent."
    → Physics Agent: "What is the speed of light in km/s?"
    
    Step 2: "Now I'll calculate the percentage using the math agent."
    → Math Agent: "What is (11 km/s) / (299,792.458 km/s) as a percentage?"
    
    Step 3: Synthesize: "A spacecraft traveling at 11 km/s moves at approximately 0.0037% of the speed of light."

    **💡 BEST PRACTICES:**
    - Always explain your reasoning to help students learn
    - Show the step-by-step process for complex problems
    - Provide context and educational value, not just answers
    - If uncertain about domain classification, ask for clarification
    - Maintain a helpful, encouraging tone throughout interactions

    **🔧 ERROR HANDLING:**
    - If an agent cannot provide the needed information, try alternative approaches
    - For ambiguous questions, ask clarifying questions
    - Always provide educational value even when direct answers aren't possible
    """,
    
    # Specialist Agents Configuration
    # These are the domain experts that the root agent can delegate to
    sub_agents=[
        maths_agent,      # Mathematical calculations and problem solving
        physics_agent,    # Physical constants, laws, and phenomena
        chemistry_agent,  # Chemical elements, reactions, and properties
    ],
    
    # Tool Configuration
    # Tools provide additional capabilities beyond the core agents
    tools=[
        AgentTool(news_analyst)  # AI news search and analysis capabilities
    ]
)
