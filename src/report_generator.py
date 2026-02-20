import os
import json
import logging
from typing import Dict
from docxtpl import DocxTemplate

def generate_qms_report(json_filepath: str, template_filepath: str, output_dir: str) -> None:
    """
    Generates a QMS report by injecting JSON data into a Word template using docxtpl.
    Args:
        json_filepath (str): Path to the JSON file containing report data.
        template_filepath (str): Path to the Word (.docx) template file with Jinja2 tags.
        output_dir (str): Directory to save the generated report.
    """
    # Check if input files exist
    if not os.path.exists(json_filepath):
        logging.error(f"JSON file not found: {json_filepath}")
        return
    if not os.path.exists(template_filepath):
        logging.error(f"Template file not found: {template_filepath}")
        return
    # Load JSON data
    try:
        with open(json_filepath, 'r', encoding='utf-8') as f:
            data: Dict = json.load(f)
    except Exception as e:
        logging.error(f"Failed to load JSON: {e}")
        return
    # Check for requirement_id in JSON
    requirement_id = data.get('requirement_id')
    if not requirement_id:
        logging.error("'requirement_id' not found in JSON data.")
        return
    # Load the Word template
    try:
        doc = DocxTemplate(template_filepath)
    except Exception as e:
        logging.error(f"Failed to load Word template: {e}")
        return
    # Render the template with JSON data
    try:
        doc.render(data)
    except Exception as e:
        logging.error(f"Failed to render template: {e}")
        return
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    output_filename = f"{requirement_id}_Final_Report.docx"
    output_path = os.path.join(output_dir, output_filename)
    # Save the generated document
    try:
        doc.save(output_path)
        logging.info(f"Report generated: {output_path}")
    except Exception as e:
        logging.error(f"Failed to save report: {e}")

if __name__ == "__main__":
    import logging # (Make sure logging is actually imported at the top of your file too!)
    logging.basicConfig(level=logging.INFO)
    
    # Corrected mocked file paths for local testing from the root directory
    json_filepath = "output_reports/test_judge.json"
    template_filepath = "skills/qa-judge/assets/qms_template.docx"
    output_dir = "output_reports"
    
    generate_qms_report(json_filepath, template_filepath, output_dir)
