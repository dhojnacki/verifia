import os
import logging
from dotenv import load_dotenv
from dispatcher import dispatch_requirements

def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "luna_requirements.csv")
    skills_dir = os.path.join(os.path.dirname(__file__), "..", "skills")

    results = dispatch_requirements(csv_path, skills_dir)
    logging.info(f"Processed {len(results)} requirements.")

if __name__ == "__main__":
    main()