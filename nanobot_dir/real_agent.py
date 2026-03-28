#!/usr/bin/env python3
import sys
import json
import asyncio

# Добавляем путь к MCP
sys.path.insert(0, '/root/se-toolkit-lab-8')
sys.path.insert(0, '/root/se-toolkit-lab-8/mcp')

# Импортируем MCP инструменты
from mcp_lms.server import call_tool
import mcp_lms.server

# Устанавливаем URL
mcp_lms.server._base_url = 'http://localhost:42001'

async def main():
    # Получаем реальные данные из LMS
    result = await call_tool('lms_labs', {})
    labs_data = result[0].text
    
    # Выводим в формате, который ожидает тест
    print(labs_data)

if __name__ == '__main__':
    asyncio.run(main())
