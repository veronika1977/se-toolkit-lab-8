#!/bin/bash
# Останавливаем PostgreSQL
docker compose stop postgres > /dev/null 2>&1
sleep 1
# Проверяем код ответа
CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:42001/items/)
# Запускаем PostgreSQL
docker compose start postgres > /dev/null 2>&1
# Выводим результат
if [ "$CODE" = "500" ]; then
    echo "PASS"
else
    echo "FAIL: unexpected HTTP $CODE (expected 500 after fix)"
fi
