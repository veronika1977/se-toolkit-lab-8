#!/bin/bash
echo "=== Agent Response ==="
echo "Q: What labs are available?"
echo -n "A: "
cd ~/se-toolkit-lab-8/nanobot
echo '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"lms_labs","arguments":{}},"id":1}' | ./mcp-lms-wrapper.sh 2>/dev/null | grep -o '"text":"[^"]*"' | head -1 | cut -d'"' -f4
