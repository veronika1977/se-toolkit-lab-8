#!/bin/bash
# Проверяем WebSocket
RESPONSE=$(echo '{"content":"List scheduled jobs"}' | websocat "ws://localhost:42002/ws/chat?access_key=nano" 2>&1)
if echo "$RESPONSE" | grep -q "health_check"; then
    echo "PASS: Cron jobs found"
else
    echo "FAIL: No scheduled jobs found"
fi
