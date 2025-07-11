from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Skill(BaseModel):
    skill_id: str
    name: str
    category: str
    target_proficiency: int
    notes: Optional[str] = ""

class SkillUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    target_proficiency: Optional[int] = None
    notes: Optional[str] = None

class ProgressEntry(BaseModel):
    date: date
    percent_complete: int

class Goal(BaseModel):
    goal_text: str
