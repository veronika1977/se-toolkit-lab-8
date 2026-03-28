#!/usr/bin/env python3
import os
import sys
print("✅ Nanobot starting...")
os.execvp("nanobot", ["nanobot", "gateway", "--config", "/app/nanobot/config.json"])
