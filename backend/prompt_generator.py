# backend/prompt_generator.py

def generate_prompt(prompt_data: dict) -> dict:
    return {
        "generated_prompt": f"Processed prompt: {prompt_data.get('input', '')}"
    }
