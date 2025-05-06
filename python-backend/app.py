from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import re

app = FastAPI()

# CORS settings for local development and Chrome extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origin for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Command(BaseModel):
    command: str

def extract_forecast_message(text: str):
    """Extract message after natural trigger like 'for this message:' or quotes."""
    # Regex to extract message between quotes or after colon
    match = re.search(r"(?:message\s*[:\-]\s*|['\"])([^'\"]{10,})['\"]?$", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

@app.post("/parse-command")
async def parse_command(command: Command):
    text = command.command.strip().lower()

    # Check if it's a forecast-related intent
    trigger_keywords = ['forecast', 'believability', 'virality', 'score']
    if any(keyword in text for keyword in trigger_keywords):
        message = extract_forecast_message(command.command)
        if message:
            return {
                "message": f"Submitting message for forecast: {message}",
                "action": "forecast",
                "raw_message": message
            }
        else:
            return {
                "message": "Could not extract a message to forecast. Please clarify.",
                "action": "none"
            }

    return {"message": "No actionable command detected.", "action": "none"}
