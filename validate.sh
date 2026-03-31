#!/bin/bash
cd /root/se-toolkit-lab-8

# Stop PostgreSQL forcefully
docker compose --env-file .env.docker.secret stop postgres -t 1 > /dev/null 2>&1
sleep 3
docker compose --env-file .env.docker.secret kill postgres > /dev/null 2>&1
sleep 5

# Verify postgres is stopped
for i in 1 2 3; do
    PG_RUNNING=$(docker inspect se-toolkit-lab-8-postgres-1 --format='{{.State.Running}}' 2>/dev/null)
    if [ "$PG_RUNNING" = "true" ]; then
        docker compose --env-file .env.docker.secret kill postgres > /dev/null 2>&1
        sleep 2
    fi
done

# Check HTTP code
CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:42001/items/ 2>/dev/null)

# Start PostgreSQL
docker compose --env-file .env.docker.secret start postgres > /dev/null 2>&1
sleep 3

# Output result
if [ "$CODE" = "500" ]; then
    echo "PASS"
    exit 0
else
    echo "FAIL: expected HTTP 500, got $CODE"
    exit 1
fi
