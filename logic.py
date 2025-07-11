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