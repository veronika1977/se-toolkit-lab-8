# Task 1 — Set Up the Agent

## Task 1A — Bare agent

**Q: What is the agentic loop?**
The agentic loop is the process where an AI agent receives a query, determines which tools to call, executes them, and feeds results back to the LLM for final response.

**Q: What labs are available in our LMS?**
I don't have access to the LMS system yet. MCP tools need to be configured.

## Task 1B — Agent with LMS tools

**Q: What labs are available?**
[{"id": 1, "type": "lab", "parent_id": null, "title": "Lab 8", "description": "Software Engineering Toolkit Lab 8"}]

**Q: Describe the architecture of the LMS system**
The LMS system consists of:
- Backend API (FastAPI) on port 42001
- PostgreSQL database on port 42004
- Caddy reverse proxy on port 42002
- MCP server for tool integration exposing tools: lms_health, lms_labs, lms_pass_rates, lms_timeline, lms_groups, lms_top_learners, lms_completion_rate, lms_sync_pipeline

## Task 1C — Skill prompt

**Q: Show me the scores**
Please specify which lab you want to see scores for. Available labs: Lab 8
