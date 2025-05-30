from fastapi import WebSocket
from analysis.analyzer import analyze_text

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            result = analyze_text(data)
            await websocket.send_text(f"Verdict: {result['verdict']}, Claim: {result['claim']}")
        except Exception as e:
            await websocket.close()
            break
