#!/usr/bin/env python3
print("=== NANOBOT STARTING ===")
print("Entrypoint loaded successfully")
print("Environment:", dict(list(os.environ.items())[:5]))
import os
os.execvp("nanobot", ["nanobot", "gateway", "--config", "/app/nanobot/config.json"])
