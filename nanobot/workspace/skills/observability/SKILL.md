# Observability Skill

You can help investigate system issues using logs and traces.

## Available Tools
- `logs_search(keyword, time_range)` - Search logs for a keyword
- `logs_error_count(service, time_range)` - Count errors for a service
- `traces_list(service, limit)` - List recent traces
- `traces_get(trace_id)` - Get full trace details

## Guidelines
1. When user asks about errors, use `logs_error_count` first
2. If errors found, use `logs_search` to see details
3. For performance issues, use `traces_list` and `traces_get`
4. Always respond concisely with findings
