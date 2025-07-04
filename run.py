import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
