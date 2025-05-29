"""
AI Tutor - Multi-Agent Learning System
=====================================

Main FastAPI application file that serves as the backend for the AI Tutor system.
This application provides a REST API for processing user queries through a 
multi-agent system powered by Google's Gemini AI.

Author: AI Tutor Team
Version: 1.0.0
License: MIT

Dependencies:
- FastAPI: Web framework for building APIs
- Google ADK: Agent Development Kit for multi-agent systems
- Google Gemini AI: Language model for intelligent responses
"""

# Standard library imports
import sys
import os
import traceback

# Third-party imports
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Google AI and ADK imports
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Load environment variables from .env file
# This must be done before importing any modules that depend on environment variables
load_dotenv()

# Add the project root to the Python path to allow importing 'multiagent'
# This ensures that the multiagent module can be imported regardless of how the app is run
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the root agent after setting up the path
from multiagent.agent import root_agent


def setup_authentication() -> bool:
    """
    Configure authentication for Google AI or Vertex AI services.
    
    This function attempts to set up authentication using either:
    1. Google AI Studio API key (recommended for development)
    2. Google Cloud Vertex AI (recommended for production)
    
    Returns:
        bool: True if authentication was successfully configured, False otherwise
        
    Environment Variables:
        GOOGLE_AI_API_KEY: API key from Google AI Studio
        GOOGLE_CLOUD_PROJECT: Google Cloud project ID for Vertex AI
        GOOGLE_CLOUD_LOCATION: Google Cloud region (defaults to 'us-central1')
    """
    # Option 1: Google AI Studio API key (recommended for development)
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    if api_key:
        print("✓ Using Google AI Studio API key for authentication")
        
        # Set the API key in multiple environment variable formats
        # This ensures compatibility with different ADK versions and configurations
        os.environ['GOOGLE_AI_API_KEY'] = api_key
        os.environ['GEMINI_API_KEY'] = api_key
        os.environ['GOOGLE_API_KEY'] = api_key
        
        # Display partial API key for verification (security: only show first 20 chars)
        print(f"✓ API key loaded successfully: {api_key[:20]}...")
        return True
    
    # Option 2: Google Cloud Vertex AI (recommended for production)
    project = os.getenv('GOOGLE_CLOUD_PROJECT')
    location = os.getenv('GOOGLE_CLOUD_LOCATION', 'us-central1')
    
    if project:
        print(f"✓ Using Vertex AI with project: {project}, location: {location}")
        # The ADK will automatically use these environment variables
        return True
    
    # If no authentication method is configured, display helpful instructions
    print("=" * 60)
    print("⚠️  AUTHENTICATION REQUIRED")
    print("=" * 60)
    print("You need to configure authentication for Google AI or Vertex AI.")
    print("\nPlease create a .env file in your project root with one of these options:")
    print("\n📝 Option 1 - Google AI Studio API Key (Recommended for development):")
    print("   GOOGLE_AI_API_KEY=your_api_key_here")
    print("   Get your API key: https://aistudio.google.com/app/apikey")
    print("\n🏢 Option 2 - Vertex AI (For production with Google Cloud):")
    print("   GOOGLE_CLOUD_PROJECT=your_project_id")
    print("   GOOGLE_CLOUD_LOCATION=us-central1")
    print("   Then run: gcloud auth application-default login")
    print("=" * 60)
    return False


# Initialize FastAPI application
app = FastAPI(
    title="AI Tutor API",
    description="Multi-Agent Learning System powered by Google Gemini AI",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI documentation
    redoc_url="/redoc"  # ReDoc documentation
)

# Global variables for application state
authentication_configured = False
session_service = None
runner = None
APP_NAME = "aitutor"

# Setup authentication and initialize services on startup
authentication_configured = setup_authentication()

if authentication_configured:
    try:
        print("🚀 Initializing AI Tutor services...")
        
        # Initialize session service for managing user conversations
        # InMemorySessionService stores sessions in memory (suitable for development)
        session_service = InMemorySessionService()
        
        # Debug: Print environment variable status (masked for security)
        print("🔐 Environment variables status:")
        env_vars = ['GOOGLE_AI_API_KEY', 'GEMINI_API_KEY', 'GOOGLE_API_KEY']
        for var in env_vars:
            status = '✓ Set' if os.getenv(var) else '✗ Not set'
            print(f"   {var}: {status}")
        
        # Initialize the ADK runner with the root agent
        # The runner manages the execution of the multi-agent system
        runner = Runner(
            agent=root_agent, 
            app_name=APP_NAME, 
            session_service=session_service
        )
        
        print("✅ AI Tutor services initialized successfully")
        
    except Exception as e:
        print(f"❌ Error initializing AI Tutor services: {e}")
        traceback.print_exc()
        authentication_configured = False
        session_service = None
        runner = None
else:
    print("⚠️  AI Tutor services not initialized due to authentication issues")


class QueryRequest(BaseModel):
    """
    Pydantic model for user query requests.
    
    This model validates and serializes incoming requests from the frontend.
    
    Attributes:
        text (str): The user's question or query text
    """
    text: str
    
    class Config:
        """Pydantic configuration for the QueryRequest model."""
        schema_extra = {
            "example": {
                "text": "What is the speed of light?"
            }
        }


@app.post("/api/query")
async def process_query_endpoint(request: QueryRequest) -> dict:
    """
    Process a user query through the multi-agent system.
    
    This endpoint receives user questions, routes them through the appropriate
    specialist agents, and returns formatted responses.
    
    Args:
        request (QueryRequest): The user's query wrapped in a Pydantic model
        
    Returns:
        dict: JSON response containing the agent's answer
        
    Raises:
        HTTPException: If the service is not properly configured
        
    Example:
        POST /api/query
        {
            "text": "Solve: 2x + 5 = 15"
        }
        
        Response:
        {
            "response": "To solve 2x + 5 = 15:\n1. Subtract 5 from both sides: 2x = 10\n2. Divide by 2: x = 5"
        }
    """
    # Check if the service is properly configured
    if not authentication_configured or not runner:
        return {
            "response": "🔧 Service not configured. Please set up Google AI API key or Vertex AI credentials in your .env file. Check the server console for setup instructions."
        }
    
    user_query = request.text.strip()
    
    # Validate input
    if not user_query:
        return {
            "response": "Please provide a valid question."
        }
    
    print(f"📝 Processing query: {user_query}")
    
    try:
        # Create a new session for this query
        # In a production environment, you might want to implement session persistence
        session = session_service.create_session(
            app_name=APP_NAME, 
            user_id="web_user"  # In production, use actual user IDs
        )
        
        # Create the user message content in the format expected by Google AI
        user_content = types.Content(
            role='user', 
            parts=[types.Part(text=user_query)]
        )
        
        # Process the query through the multi-agent system
        response_text = ""
        async for event in runner.run_async(
            user_id="web_user", 
            session_id=session.id, 
            new_message=user_content
        ):
            # Collect the final response from the agent system
            if event.is_final_response() and event.content and event.content.parts:
                response_text = event.content.parts[0].text
                break
        
        # Fallback response if no content was generated
        if not response_text:
            response_text = "I apologize, but I couldn't process your question right now. Please try rephrasing your question or try again later."
            
        print(f"✅ Query processed successfully")
        return {"response": response_text}
        
    except Exception as e:
        # Log the error for debugging
        print(f"❌ Error processing query: {e}")
        traceback.print_exc()
        
        # Return user-friendly error message
        return {
            "response": "I encountered an error while processing your question. Please try again later or contact support if the issue persists."
        }


# Static file serving configuration
# Mount the static directory to serve HTML, CSS, JavaScript, and other assets
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root() -> HTMLResponse:
    """
    Serve the main application interface.
    
    This endpoint serves the main HTML file that contains the AI Tutor frontend.
    The frontend provides a modern chat interface for interacting with the
    multi-agent system.
    
    Returns:
        HTMLResponse: The main HTML page with the AI Tutor interface
        
    Raises:
        HTTPException: If the HTML file cannot be read
    """
    try:
        # Read the main HTML file with explicit UTF-8 encoding
        # This ensures proper handling of special characters and emojis
        with open("static/index.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        
        return HTMLResponse(content=html_content)
    
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, 
            detail="Frontend not found. Please ensure static/index.html exists."
        )
    except Exception as e:
        print(f"❌ Error serving frontend: {e}")
        raise HTTPException(
            status_code=500, 
            detail="Internal server error while loading the application."
        )


# Health check endpoint for monitoring and deployment
@app.get("/health")
async def health_check() -> dict:
    """
    Health check endpoint for monitoring service status.
    
    Returns:
        dict: Service health status and configuration info
    """
    return {
        "status": "healthy" if authentication_configured else "degraded",
        "service": "AI Tutor",
        "version": "1.0.0",
        "authentication": "configured" if authentication_configured else "not_configured",
        "agents": ["mathematics", "physics", "chemistry", "news_analyst"] if runner else []
    }


if __name__ == "__main__":
    import uvicorn
    
    # Run the application if this file is executed directly
    # For production, use a proper WSGI server like Gunicorn
    print("🚀 Starting AI Tutor development server...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload for development
        log_level="info"
    )
