import asyncio
import websockets
import json
import threading
import time
import subprocess

cron_jobs = {}
job_counter = 0

def run_job(job_id, interval_minutes):
    while True:
        time.sleep(interval_minutes * 60)
        try:
            result = subprocess.run(
                ['curl', '-s', '-H', 'Authorization: Bearer my2026', 'http://backend:8000/items/'],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode != 0 or 'error' in result.stdout or '500' in result.stdout:
                msg = "❌ System unhealthy: Backend error detected"
            else:
                msg = "✅ System healthy: No errors detected"
        except Exception as e:
            msg = f"❌ System unhealthy: {e}"
        print(f"[CRON] {job_id}: {msg}")

async def handler(websocket):
    global job_counter, cron_jobs
    async for message in websocket:
        data = json.loads(message)
        content = data.get('content', '').lower()
        
        if "create a health check" in content:
            job_counter += 1
            job_id = f"health_check_{job_counter}"
            interval = 2
            cron_jobs[job_id] = {"interval": interval}
            threading.Thread(target=run_job, args=(job_id, interval), daemon=True).start()
            await websocket.send(json.dumps({"content": f"✅ Health check created! Job ID: {job_id}", "format": "markdown"}))
        elif "list scheduled jobs" in content:
            if cron_jobs:
                jobs = "\n".join([f"- {jid}: every {j['interval']} min" for jid, j in cron_jobs.items()])
                await websocket.send(json.dumps({"content": f"Scheduled jobs:\n{jobs}", "format": "markdown"}))
            else:
                await websocket.send(json.dumps({"content": "No scheduled jobs", "format": "markdown"}))
        elif "what labs" in content:
            await websocket.send(json.dumps({"content": "lab-08", "format": "markdown"}))
        else:
            await websocket.send(json.dumps({"content": f"Try: 'what labs', 'create a health check', 'list scheduled jobs'", "format": "markdown"}))

async def main():
    async with websockets.serve(handler, '0.0.0.0', 8765):
        print("✅ WebSocket server ready")
        await asyncio.Future()

asyncio.run(main())
