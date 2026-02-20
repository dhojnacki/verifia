import os
import logging
import pandas as pd
from agents import SpecialistAgent
from typing import List, Dict

def dispatch_requirements(csv_path: str, skills_dir: str) -> List[Dict]:
    if not os.path.exists(csv_path):
        logging.error(f"Requirements CSV not found: {csv_path}")
        return []

    df = pd.read_csv(csv_path)
    results = []

    for _, row in df.iterrows():
        sub_method = str(row.get("Sub_Method", "")).strip()
        requirement_text = str(row.get("Requirement_Text", ""))
        evidence_file_path = str(row.get("Evidence_File_Path", ""))
        # Normalize sub_method to folder name (e.g., "Labeling Review" -> "labeling-review")
        skill_folder = sub_method.lower().replace(" ", "-")
        skill_prompt_path = os.path.join(skills_dir, skill_folder, "SKILL.md")

        agent = SpecialistAgent(
            requirement_text=requirement_text,
            evidence_file_path=evidence_file_path,
            skill_prompt_path=skill_prompt_path
        )
        agent_response = agent.run()
        results.append(agent_response)

    return results