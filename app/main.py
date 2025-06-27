from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

# ✅ Load environment variables from .env (if any)
load_dotenv()

# ✅ Create FastAPI app
app = FastAPI()

# ✅ Mount static folder for CSS, JS, images
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ Set Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# ✅ Import route modules (corrected to your structure)
from routes import eco, chat, feedback, city_health, summarizer

# ✅ Home route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ✅ Register routers
app.include_router(eco.router)
app.include_router(chat.router)
app.include_router(feedback.router)
app.include_router(city_health.router)
app.include_router(summarizer.router)
