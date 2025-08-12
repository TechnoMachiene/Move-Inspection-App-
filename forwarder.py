# forwarder.py
import os
import base64
from typing import Optional
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import RedirectResponse
import httpx
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Image -> n8n Forwarder")

# Allow all origins for testing (you can tighten later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5500"] if using VSCode Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Config
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "http://localhost:5678/webhook-test/inspection1")
MODE = os.getenv("FORWARD_MODE", "multipart").lower()

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.post("/analyze")
async def analyze_images(
    movein: UploadFile = File(...),
    moveout: UploadFile = File(...),
    forward_mode: Optional[str] = None
):
    """Upload both move-in and move-out images and send to n8n for analysis"""
    chosen_mode = (forward_mode or MODE).lower()

    try:
        movein_data = {
            "filename": movein.filename,
            "content": await movein.read(),
            "content_type": movein.content_type or "application/octet-stream"
        }
        moveout_data = {
            "filename": moveout.filename,
            "content": await moveout.read(),
            "content_type": moveout.content_type or "application/octet-stream"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read images: {e}")

    async with httpx.AsyncClient(timeout=60) as client:
        if chosen_mode == "multipart":
            files = {
                "image_movein": (movein_data["filename"], movein_data["content"], movein_data["content_type"]),
                "image_moveout": (moveout_data["filename"], moveout_data["content"], moveout_data["content_type"]),
            }
            resp = await client.post(N8N_WEBHOOK_URL, files=files)
            return {
                "forward_mode": "multipart",
                "n8n_status_code": resp.status_code,
                "n8n_response_text": resp.text,
            }

        elif chosen_mode == "json":
            movein_b64 = base64.b64encode(movein_data["content"]).decode("ascii")
            moveout_b64 = base64.b64encode(moveout_data["content"]).decode("ascii")

            payload = {
                "image_movein_base64": f"data:{movein_data['content_type']};base64,{movein_b64}",
                "image_moveout_base64": f"data:{moveout_data['content_type']};base64,{moveout_b64}",
            }
            resp = await client.post(N8N_WEBHOOK_URL, json=payload)
            return {
                "forward_mode": "json",
                "n8n_status_code": resp.status_code,
                "n8n_response_text": resp.text,
            }

        else:
            raise HTTPException(status_code=400, detail=f"Unknown forward_mode: {chosen_mode}")