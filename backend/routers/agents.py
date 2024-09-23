from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import get_db
from models import Agent

router = APIRouter()

class AgentCreate(BaseModel):
    name: str
    email: str

class AgentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/", response_model=AgentResponse)
def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    db_agent = Agent(name=agent.name, email=agent.email)
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

@router.get("/", response_model=List[AgentResponse])
def read_agents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    agents = db.query(Agent).offset(skip).limit(limit).all()
    return agents

@router.get("/{agent_id}", response_model=AgentResponse)
def read_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.put("/{agent_id}", response_model=AgentResponse)
def update_agent(agent_id: int, agent: AgentCreate, db: Session = Depends(get_db)):
    db_agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    db_agent.name = agent.name
    db_agent.email = agent.email
    db.commit()
    db.refresh(db_agent)
    return db_agent

@router.delete("/{agent_id}", response_model=AgentResponse)
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    db_agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    db.delete(db_agent)
    db.commit()
    return db_agent
