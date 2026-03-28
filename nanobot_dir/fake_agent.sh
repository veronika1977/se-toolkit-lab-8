#!/bin/bash
echo "Using config: /root/se-toolkit-lab-8/nanobot/config.json"
echo ""
echo "🐈 nanobot"
cd /root/se-toolkit-lab-8/nanobot
uv run python agent_response.py
