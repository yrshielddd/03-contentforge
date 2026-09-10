# ContentForge

ContentForge is a multi-stage AI content generation workflow built with Python and local LLM inference.

The project demonstrates how a complex content task can be decomposed into independent AI stages and orchestrated as a reproducible pipeline.

## Workflow

```text
Topic
  ↓
Researcher
  ↓
Strategist
  ↓
Writer
  ↓
Editor
  ↓
Fact Checker
  ↓
Final Output
````

Each stage uses a separate skill definition stored as a Markdown file.

## Project Structure

```text
03-contentforge/
├── skills/
│   ├── researcher.md
│   ├── strategist.md
│   ├── writer.md
│   ├── editor.md
│   └── fact_checker.md
├── main.py
├── orchestrator.py
├── requirements.txt
└── .gitignore
```

## Skills

* `researcher.md` defines the research stage.
* `strategist.md` creates the content strategy and structure.
* `writer.md` generates the initial draft.
* `editor.md` performs structural and stylistic editing.
* `fact_checker.md` performs a separate verification pass.

The skills are kept separate from the orchestration logic so that individual stages can be modified without changing the entire workflow.

## Technical Stack

* Python
* FastAPI
* Pydantic
* Requests
* Ollama
* Llama 3.2 3B
* Markdown-based AI skills

## API

Start the local API:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### Generate Content

`POST /generate`

Request:

```json
{
  "topic": "How remote work is changing modern careers"
}
```

The endpoint executes the complete five-stage workflow and returns the output of each stage.

## Architecture

The main orchestration logic is implemented in `orchestrator.py`.

The workflow:

1. Loads the corresponding skill definition.
2. Combines the skill instructions with the current workflow input.
3. Sends the request to the local Ollama model.
4. Passes the result to the next stage.
5. Returns all intermediate outputs as structured data.

This approach demonstrates task decomposition, prompt modularity, sequential AI orchestration, and separation of generation from quality-control stages.

## Purpose

ContentForge was created as a portfolio project demonstrating practical AI workflow development, prompt engineering, AI-assisted automation, and integration of multiple specialized AI stages into a single application.
