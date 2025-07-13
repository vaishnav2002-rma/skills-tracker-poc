from data import skills, progress_logs, goals
from schemas import Skill, ProgressEntry, Goal

def add_skill(skill: Skill):
    if skill.skill_id in skills:
        return False
    skills[skill.skill_id] = skill
    progress_logs[skill.skill_id] = []
    goals[skill.skill_id] = []
    return True

def get_all_skills():
    return skills

def get_skill(skill_id: str):
    return skills.get(skill_id)

def update_skill(skill_id: str, update_data: dict):
    if skill_id not in skills:
        return None
    existing_skill = skills[skill_id]  # This is a Skill model
    updated_skill = existing_skill.copy(update=update_data)  # Proper Pydantic update

    skills[skill_id] = updated_skill
    return updated_skill

def delete_skill(skill_id: str):
    if skill_id in skills:
        skills.pop(skill_id)
        progress_logs.pop(skill_id)
        goals.pop(skill_id)
        return True
    return False

def log_progress(skill_id: str, entry: ProgressEntry):
    if skill_id not in progress_logs:
        return False
    progress_logs[skill_id].append(entry)
    return True