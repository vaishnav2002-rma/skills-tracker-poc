from fastapi import FastAPI, HTTPException
from schemas import Skill, SkillUpdate, ProgressEntry, Goal
from logic import (
    add_skill, get_all_skills, get_skill, update_skill
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

@app.get("/skills/{skill_id}")
async def read_skill(skill_id: str):
    skill = get_skill(skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill

@app.put("/skills/{skill_id}")
async def modify_skill(skill_id: str, update: SkillUpdate):
    updated = update_skill(skill_id, update.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Skill not found")
    return updated