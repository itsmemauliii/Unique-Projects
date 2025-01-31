import json
from collections import Counter

def suggest_careers(skills, interests, career_data):
    """
    Suggests career paths based on user skills & interests.
    """
    skills_list = skills.lower().split(",")
    interests_list = interests.lower().split(",")

    career_scores = {}

    for career, details in career_data.items():
        skill_match = sum(1 for skill in skills_list if skill.strip() in details["skills"])
        interest_match = sum(1 for interest in interests_list if interest.strip() in details["interests"])
        
        # Weighted scoring
        score = (skill_match * 2) + interest_match
        career_scores[career] = score

    # Rank and return top 3 matches
    ranked_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    return [(career, round(score / max(career_scores.values()) * 100, 1)) for career, score in ranked_careers[:3]]
