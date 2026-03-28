#!/usr/bin/env python3
import os
import sys

print("=== NANOBOT GATEWAY STARTING ===")
print(f"Config: /app/nanobot/config.json")
print(f"Workspace: /app/nanobot/workspace")

# Запускаем nanobot gateway
os.execvp("nanobot", ["nanobot", "gateway", "--config", "/app/nanobot/config.json", "--workspace", "/app/nanobot/workspace"])
