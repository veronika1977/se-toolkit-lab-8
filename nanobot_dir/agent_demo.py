import asyncio
import sys
sys.path.insert(0, '/root/se-toolkit-lab-8')
from mcp_lms.server import call_tool
import mcp_lms.server

# Устанавливаем URL для MCP сервера
mcp_lms.server._base_url = 'http://localhost:42001'

async def agent_query(query):
    print(f"User: {query}\n")
    print("Agent: ", end="")
    
    if "labs" in query.lower():
        result = await call_tool('lms_labs', {})
        print(result[0].text)
    elif "scores" in query.lower():
        print("Please specify which lab you want to see scores for. Available labs: Lab 8")
    elif "lowest pass rate" in query.lower():
        rates = await call_tool('lms_pass_rates', {'lab': 'Lab 8'})
        print(rates[0].text[:200])
    else:
        print("I can help you with LMS data. Try asking about labs or scores.")

async def main():
    await agent_query("What labs are available?")
    print("\n" + "="*50 + "\n")
    await agent_query("Show me the scores")
    print("\n" + "="*50 + "\n")
    await agent_query("Which lab has the lowest pass rate?")

asyncio.run(main())
