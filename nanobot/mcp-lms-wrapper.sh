#!/usr/bin/env bash
export NANOBOT_LMS_API_KEY="my2026"
export PYTHONPATH="/Users/veronikadrozd/software-engineering-toolkit/se-toolkit-lab-8/mcp:$PYTHONPATH"
exec python -m mcp_lms http://localhost:42002
