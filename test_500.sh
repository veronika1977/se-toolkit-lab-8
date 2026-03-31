#!/bin/bash
cd /root/se-toolkit-lab-8

# Stop PostgreSQL
docker compose --env-file .env.docker.secret stop postgres > /dev/null 2>&1
sleep 8

# Check HTTP code
CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:42001/items/ 2>/dev/null)

# Start PostgreSQL
docker compose --env-file .env.docker.secret start postgres > /dev/null 2>&1
sleep 3

# Output result
if [ "$CODE" = "500" ]; then
    echo "PASS"
else
    echo "FAIL: expected HTTP 500, got $CODE"
fi
