# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Question 1: "What is the agentic loop?"**

The agentic loop is the fundamental cycle that AI agents follow to accomplish tasks autonomously. It typically consists of these core stages:

1. **Perceive** — Gather information from the environment (user input, files, APIs, sensors, etc.)
2. **Reason/Plan** — Analyze the information, determine goals, and decide on actions to take
3. **Act** — Execute actions using available tools (write files, run commands, call APIs, send messages, etc.)
4. **Observe** — Receive feedback from the actions taken (outputs, errors, state changes)
5. **Repeat** — Loop back to step 1 with the new information, continuing until the goal is achieved

This loop enables agents to work autonomously toward goals, adapt to changing conditions, handle multi-step tasks, and learn from feedback and correct mistakes.

**Question 2: "What labs are available in our LMS?"**

The agent (without tools) looked at the file system and found the lab directory structure, listing:

- Task 1: Set Up the Agent
- Task 2: Deploy and Connect a Web Client
- Task 3: Give the Agent New Eyes
- Task 4: Diagnose a Failure and Make the Agent Proactive
- Optional Task 1: Add a Telegram Bot Client

Note: The agent does not have access to the actual LMS backend data yet — it was reading from the file system.

## Task 1B — Agent with LMS tools

**Question 1: "What labs are available in the LMS?"**

The agent (with MCP tools) returned real data from the LMS backend:

✅ Backend is healthy with 56 items total. Available labs:

| ID | Lab Title |
|----|-----------|
| 1 | Lab 01 – Products, Architecture & Roles |
| 2 | Lab 02 — Run, Fix, and Deploy a Backend Service |
| 3 | Lab 03 — Backend API: Explore, Debug, Implement, Deploy |
| 4 | Lab 04 — Testing, Front-end, and AI Agents |
| 5 | Lab 05 — Data Pipeline and Analytics Dashboard |
| 6 | Lab 06 — Build Your Own Agent |
| 7 | Lab 07 — Build a Client with an AI Coding Agent |
| 8 | lab-08 (The Agent is the Interface) |

**Question 2: "Describe the architecture of the LMS system"**

The agent provided a detailed architecture description including:

- **Client Layer**: React Web Dashboard, Flutter Web Chat, Telegram Bot (optional)
- **Gateway Layer**: Caddy reverse proxy (port 42002)
- **Application Layer**: LMS Backend (FastAPI, port 42001), Nanobot Agent (port 18790/8765), Qwen Code API (port 42005)
- **Data Layer**: PostgreSQL (port 42004), pgAdmin (port 42003)
- **Observability Stack**: OpenTelemetry Collector, VictoriaLogs (port 42010), VictoriaTraces (port 42011)

The agent correctly identified all services and their relationships, including the MCP tools pattern for extending agent capabilities.

## Task 1C — Skill prompt

**Question: "Show me the scores" (without specifying a lab)**

The agent (with the LMS skill prompt) now handles this correctly:

Instead of hallucinating or saying it doesn't know, the agent:
1. Called `lms_labs` to get all available labs
2. Iterated through each lab calling `lms_pass_rates` 
3. Presented a comprehensive table with all lab scores
4. Added a summary showing:
   - Highest/lowest scores per lab
   - Most attempted tasks
   - Toughest task overall (Lab 02 - "Make your VM a proxy" at 0.0%)
   - Best performing lab (Lab 07)

The skill prompt taught the agent to:
- Ask for clarification when a lab parameter is missing (or show all if appropriate)
- Format percentages with one decimal place
- Use tables for multiple items
- Offer summary statistics
- Use emojis sparingly (📊 for data, 📈 for summary, ⚠️ for warnings)

## Task 2A — Deployed agent

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
