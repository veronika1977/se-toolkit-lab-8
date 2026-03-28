import asyncio
import sys
import json
sys.path.insert(0, '/root/se-toolkit-lab-8')
from mcp_lms.server import list_tools, call_tool

async def test():
    print("Testing MCP LMS Server...")
    print("=" * 50)
    
    print("\n1. Listing tools...")
    tools = await list_tools()
    for tool in tools:
        print(f"   ✓ {tool.name}: {tool.description[:60]}...")
    
    print("\n2. Calling lms_labs...")
    try:
        result = await call_tool("lms_labs", {})
        print(f"   ✓ Result: {result[:300]}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    print("\n3. Calling lms_health...")
    try:
        result = await call_tool("lms_health", {})
        print(f"   ✓ Result: {result[:200]}")
    except Exception as e:
        print(f"   ✗ Error: {e}")

asyncio.run(test())
