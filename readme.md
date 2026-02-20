Verifia is an automated engineering tool designed to streamline the verification of the inspection/analysis/by children type of requirements. It combines determinisitc routing with AI agents to analyze the requirement and generate a .docx on template F0176.

🏗 Architecture Overview
The system follows a Deterministic Agentic Workflow. Unlike standard "black-box" AI, Verifia uses Python to control the flow of data, ensuring that AI agents only see the specific evidence and rules required for a single task.

main.py: The entry point that initializes the environment and triggers the pipeline.

dispatcher.py (The Router): Reads the requirements.csv, identifies the Sub_Method, and fetches the corresponding SKILL.md and objective evidence (PDFs/Images).

agents.py (The Specialists): Specialized AI personas (e.g., Drawing Reviewer, Labeling Specialist) that analyze evidence against specific requirement text.

qa-judge (The Compliance Filter): A secondary AI layer that audits the specialist's verdict and translates technical rationale into formal engineering prose.

report_generator.py: A deterministic document builder that injects the final analysis into a corporate Microsoft Word template.

🚀 Getting Started
Prerequisites
Python 3.8+

Microsoft Word (for template management)

Access to a virtual environment (venv)

Installation
Clone the repository to your local machine.

Activate your virtual environment:

Bash
.\venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Running the Pipeline
To process the requirements listed in data/requirements.csv:

Bash
python src/main.py
To test the document generator independently with mocked data:

Bash
python src/report_generator.py
📂 Project Structure
src/: Core logic and Python scripts.

skills/: Contains SKILL.md rulebooks and .docx templates for each agent type.

output_reports/: Final generated JSON verdicts and .docx TCN reports.

data/: Source CSV files containing requirement definitions.

assets/: Shared corporate style guides and reference materials.

🛠 Skills & Agents
Verifia uses a modular "Skill" system. Each skill folder contains:

SKILL.md: The system prompt that defines the AI's persona, constraints, and SOP.

assets/: Specific templates (e.g., qms_template.docx) used by that skill's judge.

Current Skills:

labeling-review: Verifies physical labels and barcodes.

drawing-review: Verifies mechanical dimensions and clearance.

qa-judge: Synthesizes raw data into formal QMS documentation.

🔒 Safety & Compliance
Deterministic Routing: AI cannot "browse" files; it only sees what the Dispatcher provides.

Hallucination Check: The QA Judge validates the Specialist's logic before final report generation.

Audit Trail: Every verification produces a JSON record of the AI's confidence score and rationale.