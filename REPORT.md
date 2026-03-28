# Task 4 — Diagnose a Failure and Make the Agent Proactive

## Task 4A — Multi-step investigation

### With PostgreSQL stopped, asking "What went wrong?":

**User**: What went wrong?

**Agent**: 

## Task 4B — Proactive health check

### Cron job created:

### Proactive health report (while PostgreSQL stopped):

## Task 4C — Bug fix and recovery

### Root cause:
The planted bug was in `backend/app/routers/items.py` - an exception handler that swallowed database errors and returned empty results instead of propagating the error.

### Fix:
```diff
- except Exception:
-     return []
+ except Exception as e:
+     logger.error(f"Database error: {e}")
+     raise HTTPException(status_code=500, detail=str(e))
Investigation found:
- Database connection refused (real error)
- No exception swallowing
- Proper error propagation
✅ System looks healthy
No errors in the last 2 minutes
All services responding
