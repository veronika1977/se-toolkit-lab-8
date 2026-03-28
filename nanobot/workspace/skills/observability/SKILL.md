# Observability Skill - Investigation Mode

When user asks "What went wrong?" or "Check system health", follow this investigation plan:

## Investigation Steps
1. **Check error logs first**: Use `logs_error_count` to see if there are recent errors
2. **Search for error details**: Use `logs_search` with keywords like "error", "exception", "failed"
3. **Extract trace IDs**: Look for trace_id patterns in log entries
4. **Fetch trace**: If a trace_id is found, use `traces_get` to see the full trace
5. **Summarize findings**: Combine log and trace evidence into a concise report

## Response Format
- Start with summary: "Investigation found X errors..."
- List key errors with timestamps
- If trace available, show where failure occurred
- End with conclusion: "The issue appears to be..."
