from fastapi import FastAPI
import requests
import json
import os
from Visualizer_DB.services.ajoutNameJson import add_user_to_json_file
from DB_Save.controller.Minio_controller import Get_file_from_minio, POST_file_in_Minio

LLMs = """
You are a skilled data analyst with expertise in SQL and PostgreSQL.

You will be given the schema of a PostgreSQL database, which includes:
- A list of tables with their columns and data types
- Optional example rows per table
- Cardinality (number of unique values) for selected columns
- Key relationships (primary keys and foreign keys), if available

Your task is to generate up to 10 meaningful and insightful visualizations that help users understand the data structure and patterns.

For each visualization, return a JSON object with:
- id: A unique number from 1 to 10
- title: A short, descriptive title of the insight
- columns: A list of columns used, in the format "table.column"
- description: A concise summary of the insight
- request_sql: A valid SQL query (PostgreSQL syntax) to extract the data
- suggested_chart: One of: bar, line, pie, scatter, boxplot, histogram

Guidelines:
- Focus on trends, comparisons, distributions, correlations, or high-level summaries
- Use joins where needed based on foreign key relationships
- Apply aggregation (e.g., COUNT, AVG, SUM) when appropriate
- Avoid using columns with high cardinality (e.g., UUIDs, IDs, free-text)
- Do not include visualizations that lack analytical value (e.g., raw ID counts)

Format:
Return only valid JSON in the following structure — no extra explanation, markdown, or text:

[
  {
    "id": 1,
    "title": "Descriptive title",
    "columns": ["table1.columnA", "table2.columnB"],
    "description": "Brief explanation of what this visualization reveals",
    "request_sql": "SELECT ... FROM ... JOIN ... WHERE ... GROUP BY ...",
    "suggested_chart": "bar"
  }
]

Available chart types:
bar, line, pie, scatter, boxplot, histogram

---

Database schema input begins below:

"""

def clean_llm_output(text: str) -> str:
    """Nettoie la réponse LLM en essayant d'extraire un JSON valide."""
    try:
        start = text.index('[')
        end = text.rindex(']') + 1
        return text[start:end]
    except ValueError:
        return text

def generate_json_via_llm(schema_txt_path: str,  user_value: str) -> list:
    # Lire le schéma
    file_stream, _ = Get_file_from_minio(schema_txt_path)
    schema_content = file_stream.read().decode("utf-8")
    # Concaténer le prompt et le schéma
    full_prompt = LLMs + "\n" + schema_content
    

    # hadi la partie dial openroute a si saad 
    response = requests.post(
        "http://host.docker.internal:11434/api/generate",  # Use Docker service name here
        json={"model": "mistral:7b", "prompt": full_prompt},
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
        

    # w hna katsala a si saad la partie dial openrouter
    except Exception as e:
        raise ValueError(f"Error parsing response: {str(e)}") from e
    if response.status_code != 200:
        raise Exception(f"Erreur API : {response.status_code} - {response.text}")

    try:
        cleaned_content = clean_llm_output(full_response_text)
        generated_json = json.loads(cleaned_content)
    except Exception as e:
        raise Exception(f"Erreur de parsing JSON : {e}")

    

    return generated_json
