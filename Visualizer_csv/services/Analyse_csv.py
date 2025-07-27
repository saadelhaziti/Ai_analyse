import subprocess
import json
from llm_engine.prepare_csv_prompt import prepare_csv_prompt_input
from llm_engine.prompt_loader import load_prompt
def analyze_and_generate_charts(input_filename: str, output_path: str = "charts.json"):
    if not input_filename.endswith('.csv'):
        raise ValueError("Input file must be a CSV.")

    variable_name = prepare_csv_prompt_input(input_filename)
    prompt = load_prompt("csv_analysis", variable_name)

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    output = result.stdout.decode("utf-8")

    try:
        charts = json.loads(output)
        with open(output_path, "w") as f:
            json.dump(charts, f, indent=2)
        return charts
    except Exception as e:
        raise ValueError(f"Error parsing response: {str(e)}") from e








#     # Metadata
#     unique_counts = df.nunique().sort_values(ascending=False).to_dict()
#     sample = df.head(5).to_string(index=False)
#     columns = df.dtypes.astype(str).to_dict()
#     corr_matrix = df.select_dtypes(include=[np.number]).corr().to_dict()

#     prompt = f"""You are a highly skilled data analyst specializing in SQL-based analysis using DuckDB for structured CSV data name {input_filename}.

# You will be provided with a dataset preview, including:
# - Column names and data types
# - First 5 rows of data
# - Number of unique values per column
# - A correlation matrix for numerical columns

# Your task is to generate **up to 10 insightful visualizations** based on this data preview.

# For each visualization, include the following:
# - `id`: A numeric identifier (1–10)
# - `title`: A concise title describing the visualization goal
# - `columns`: List of column names used
# - `actions`: Aggregation or transformation actions used (e.g., `SUM(actual_price)`, `COUNT(*)`, etc.)
# - `description`: Short explanation of the insight provided
# - `request_sql`: A valid DuckDB SQL query using the `data` table that prepares the data for visualization
# - `suggested_chart`: One of the following chart types: `bar`, `line`, `histogram`, `pie`, `scatter`, `boxplot`

# Guidelines:
# - Focus on relationships between time, volume, numeric trends, or categorical breakdowns.
# - Use only columns with low or medium cardinality (avoid IDs, free text, or high-uniqueness fields).
# - Prioritize visualizations that show change over time, category distributions, or statistical variation.
# - Ensure SQL queries use proper aggregation and are valid for a flat table called `data`.

# Do not generate visualizations:
# - With only high-cardinality columns (e.g., `user_id`, `invoice_no`)
# - Involving only categorical columns with too many unique values
# - Using free-text or irrelevant columns with unclear summarization value

# Output must be a list of JSON objects using the **exact structure** shown below — no commentary or explanation outside of the JSON:

# [
#   {{
#     "id": 1,
#     "title": "title of the visualization",
#     "columns": ["column1", "column2"],
#     "actions": ["actions_column1", "actions_column2"],
#     "description": "",
#     "request_sql": "",
#     "suggested_chart": ""
#   }},
#   ...
# ]
# You may use these chart types:
# - "area charts", "Pie charts", "Radar chart", "Radial Chart", "bar charts"
# Sample Rows:
# {sample}

# Column Types:
# {columns}

# Unique Value Counts:
# {unique_counts}

# Correlation Matrix (Numerical Only):
# {corr_matrix}"""  # prompt unchanged