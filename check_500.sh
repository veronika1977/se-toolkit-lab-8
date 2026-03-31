#!/bin/bash
cd /root/se-toolkit-lab-8
docker compose --env-file .env.docker.secret stop postgres > /dev/null 2>&1
sleep 5
CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:42001/items/ 2>/dev/null)
docker compose --env-file .env.docker.secret start postgres > /dev/null 2>&1
if [ "$CODE" = "500" ]; then
    echo "PASS"
    exit 0
else
    echo "FAIL: expected HTTP 500, got $CODE"
    exit 1
fi
