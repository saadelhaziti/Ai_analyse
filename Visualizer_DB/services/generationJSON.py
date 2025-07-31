from fastapi import FastAPI
import requests
import json
import os
from Visualizer_DB.services.ajoutNameJson import add_user_to_json_file
from DB_Save.controller.Minio_controller import Get_file_from_minio, POST_file_in_Minio

LLMs = """
You are a highly skilled data analyst specializing in SQL-based analysis using PostgreSQL.

You will be provided with the **schema of a PostgreSQL database**, including:
- The list of tables and their corresponding columns and data types
- A few example rows per table (optional)
- Cardinality (number of unique values) for selected columns
- Information about relationships (foreign keys, primary keys) if available

Your task is to generate **up to 10 insightful visualizations** based on this schema.

For each visualization, include the following:
- `id`: A numeric identifier from 1 to 10
- `title`: A short, descriptive title of what the visualization shows
- `columns`: A list of the involved columns in format `table.column`
- `description`: A short explanation of the insight gained from the visualization
- `request_sql`: A valid PostgreSQL SQL query that prepares the data, using standard syntax (JOINs allowed if needed)
- `suggested_chart`: One of the following: `bar`, `line`, `pie`, `scatter`, `boxplot`, `histogram`

Guidelines:
- Focus on trends, category distributions, correlations, or useful breakdowns
- Avoid columns with high cardinality (e.g., UUIDs, IDs, free text)
- Prioritize columns with interpretable categorical or numerical data
- You may join tables based on foreign key relationships if logical
- Use aggregation when appropriate (e.g., COUNT, AVG, SUM)

Do not generate visualizations:
- That rely on only raw IDs or meaningless string blobs
- That don’t provide insight or actionable understanding

**Use the following exact JSON format only** (no Markdown, explanation, or commentary):

[
  {
    "id": 1,
    "title": "Descriptive title",
    "columns": ["table1.columnA", "table2.columnB"],
    "description": "Short explanation of the insight",
    "request_sql": "SELECT ... FROM table1 JOIN table2 ON ... WHERE ... GROUP BY ...",
    "suggested_chart": "bar"
  }
]

You may use these chart types: "bar", "line", "pie", "scatter", "boxplot", "histogram"

---

**Database Schema Provided:**

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
        json={"model": "mistral", "prompt": full_prompt},
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

    charts = json.loads(full_response_text)

    try:
        cleaned_content = clean_llm_output(charts)
        generated_json = json.loads(cleaned_content)
    except Exception as e:
        raise Exception(f"Erreur de parsing JSON : {e}")

    

    return generated_json
