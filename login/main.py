import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import asyncpg
import uvicorn
from dotenv import load_dotenv

# Load .env file
load_dotenv()

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory=".")

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Function to get DB connection
async def get_db_connection():
    return await asyncpg.connect(DATABASE_URL)

@app.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    conn = await get_db_connection()
    existing_user = await conn.fetchrow("SELECT * FROM users WHERE name = $1", username)
    
    if existing_user:
        await conn.close()
        return JSONResponse(content={"status": "fail", "message": "Username already exists. Please choose another."})
    
    await conn.execute("INSERT INTO users (name, password) VALUES ($1, $2)", username, password)
    await conn.close()
    
    return JSONResponse(content={"status": "success", "message": "User registered successfully!", "redirect_url": "http://localhost:8001"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
