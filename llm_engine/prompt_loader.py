import os
import json
from jinja2 import Environment, FileSystemLoader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_DIR = os.path.join(BASE_DIR,"prompts")
# REGISTRY_FILE = "./prompt_registry.json"

REGISTRY_FILE = os.path.join(BASE_DIR, "prompt_registry.json")

env = Environment(loader=FileSystemLoader(PROMPT_DIR))

def load_prompt(prompt_key: str, variables: dict) -> str:
    # Load prompt registry
    with open(REGISTRY_FILE) as f:
        registry = json.load(f)

    if prompt_key not in registry:
        raise ValueError(f"Prompt '{prompt_key}' not found in registry.")

    prompt_meta = registry[prompt_key]
    template_file = prompt_meta["file"]
    required_vars = prompt_meta["variables"]

    # Validate that all required variables are provided
    missing = [var for var in required_vars if var not in variables]
    if missing:
        raise ValueError(f"Missing variables: {missing}")

    # Render the prompt
    template = env.get_template(template_file)
    return template.render(**variables)
