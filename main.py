from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Mount static directory for CSS, JS, images (if any)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ Set template directory for HTML files
templates = Jinja2Templates(directory="templates")

# ✅ Import all route modules
from app.routes import eco, chat, feedback, city_health, summarizer

# ✅ Homepage route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ✅ Register all routers
app.include_router(eco.router)
app.include_router(chat.router)
app.include_router(feedback.router)
app.include_router(city_health.router)
app.include_router(summarizer.router)
