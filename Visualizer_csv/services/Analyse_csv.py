import requests
import json
from llm_engine.prepare_csv_prompt import prepare_csv_prompt_input
from llm_engine.prompt_loader import load_prompt
def analyze_and_generate_charts(input_filename: str):
    if not input_filename.endswith('.csv'):
        raise ValueError("Input file must be a CSV.")

    variable_name = prepare_csv_prompt_input(input_filename)
    prompt = load_prompt("csv_analysis", variable_name)
    response = requests.post(
        "http://ollama:11434/api/generate",  # Use Docker service name here
        json={"model": "mistral:7b", "prompt": prompt},
        stream=True
    )
    if response.status_code != 200:
        raise ValueError(f"Failed to call Ollama API: {response.text}")
    full_response_text = ""
    try:
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                # Append the 'response' part to full text
                full_response_text += data.get("response", "")
        charts = json.loads(full_response_text)
        
        return charts
    except Exception as e:
        raise ValueError(f"Error parsing response: {str(e)}") from e



