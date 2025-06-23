import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def explain_tasks_individually(tasks: list[str]) -> dict:
    if not tasks:
        return {}

    prompt = (
        "For each of the following tasks, write a 1-line concise explanation like this:\n"
        "- Task: Explanation\n\n"
        + "\n".join(f"- {task}" for task in tasks)
    )

    try:
        response = model.generate_content([prompt])
        output = response.text.strip()
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return {}

    # Parse the Gemini output
    result = {}
    for line in output.splitlines():
        if ": " in line:
            task, explanation = line.split(": ", 1)
            result[task.strip("•- ").strip()] = explanation.strip()

    return result

def summarize_tasks(tasks: list[str]) -> str:
    if not tasks:
        return "1. NA"

    prompt = (
        "Summarize the following work tasks into a clear, short bullet list (1–2 lines per task):\n\n"
        + "\n".join(f"- {t}" for t in tasks)
    )

    try:
        response = model.generate_content([prompt])
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "1. NA"
