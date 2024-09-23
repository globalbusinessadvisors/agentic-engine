from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from supabase import create_client, Client
import openai
import os

from routers import agents, employment, reports, ai

# Create FastAPI application instance
app = FastAPI()

# Set up CORS middleware
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure database connection using supabase
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Integrate OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Include routes for agent management, employment, reporting, and AI interactions
app.include_router(agents.router, prefix="/agents", tags=["agents"])
app.include_router(employment.router, prefix="/employment", tags=["employment"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])
app.include_router(ai.router, prefix="/ai", tags=["ai"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Agentic Engine"}
