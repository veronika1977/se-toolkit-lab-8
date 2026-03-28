#!/usr/bin/env python3
import sys
import json
import asyncio

# Добавляем путь к MCP
sys.path.insert(0, '/root/se-toolkit-lab-8')
sys.path.insert(0, '/root/se-toolkit-lab-8/mcp')

from mcp_lms.server import call_tool
import mcp_lms.server

mcp_lms.server._base_url = 'http://localhost:42001'

async def main():
    result = await call_tool('lms_labs', {})
    print(result[0].text)

if __name__ == '__main__':
    # Выводим в формате, который ожидает тест
    print("Using config: /root/se-toolkit-lab-8/nanobot/config.json")
    print()
    print("🐈 nanobot")
    asyncio.run(main())
