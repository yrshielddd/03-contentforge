from pathlib import Path

import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"

SKILLS_DIR = Path(__file__).parent / "skills"


def load_skill(name: str) -> str:
    path = SKILLS_DIR / f"{name}.md"
    return path.read_text(encoding="utf-8")


def run_ai(skill_name: str, input_text: str) -> str:
    skill = load_skill(skill_name)

    prompt = f"""
{skill}

INPUT:
{input_text}

Perform your assigned stage and return only the requested output.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=180,
    )

    response.raise_for_status()

    return response.json()["response"].strip()


def run_content_workflow(topic: str) -> dict:
    research = run_ai(
        "researcher",
        f"Research the following topic:\n{topic}",
    )

    strategy = run_ai(
        "strategist",
        f"""
TOPIC:
{topic}

RESEARCH:
{research}
""",
    )

    draft = run_ai(
        "writer",
        f"""
TOPIC:
{topic}

RESEARCH:
{research}

CONTENT STRATEGY:
{strategy}
""",
    )

    edited = run_ai(
        "editor",
        f"""
RESEARCH:
{research}

CONTENT STRATEGY:
{strategy}

DRAFT:
{draft}
""",
    )

    fact_check = run_ai(
        "fact_checker",
        f"""
RESEARCH:
{research}

EDITED DRAFT:
{edited}
""",
    )

    return {
        "topic": topic,
        "research": research,
        "strategy": strategy,
        "draft": draft,
        "edited": edited,
        "fact_check": fact_check,
    }