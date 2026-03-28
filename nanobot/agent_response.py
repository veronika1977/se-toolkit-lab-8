import asyncio
import sys

# Добавляем пути
sys.path.insert(0, '/root/se-toolkit-lab-8')
sys.path.insert(0, '/root/se-toolkit-lab-8/mcp')

from mcp_lms.server import call_tool
import mcp_lms.server

# Устанавливаем URL
mcp_lms.server._base_url = 'http://localhost:42001'

async def main():
    result = await call_tool('lms_labs', {})
    print(result[0].text)

asyncio.run(main())
