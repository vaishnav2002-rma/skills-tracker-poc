from fastapi import FastAPI, HTTPException
from schemas import Skill, SkillUpdate, ProgressEntry, Goal
from logic import (
    add_skill, get_all_skills
)

app = FastAPI()

@app.post("/skills")
async def create_skill(skill: Skill):
    if not add_skill(skill):
        raise HTTPException(status_code=400, detail="Skill ID already exists")
    return {"message": "Skill added"}

@app.get("/skills")
async def read_all_skills():
    return get_all_skills()