import uvicorn
from fastapi import FastAPI, Depends, Request, HTTPException, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models

import requests
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory=".")

# Create tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.name == username, models.User.password == password).first()
    if user:
        return RedirectResponse(url=f"/welcome?name={user.name}", status_code=303)
    else:
        return JSONResponse(content={"status": "fail", "message": "Invalid username or password"})

@app.get("/welcome")
def welcome_page(request: Request, name: str = "Guest"):
    return templates.TemplateResponse("welcome.html", {"request": request, "name": name})

@app.get("/page/{page_name}")
def serve_dynamic_page(request: Request, page_name: str, name: str = "Guest"):
    template_path = f"{page_name}.html"
    try:
        return templates.TemplateResponse(template_path, {"request": request, "name": name})
    except:
        raise HTTPException(status_code=404, detail="Page not found")

@app.get("/check_user")
def check_user(name: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.name == name).first()
    return {"exists": user is not None}

SPRING_BOOT_API = "http://127.0.0.1:8080/api/events"

@app.get("/events", response_class=HTMLResponse)
def get_events(request: Request):
    try:
        response = requests.get(SPRING_BOOT_API)
        response.raise_for_status()
        events = response.json()
        return templates.TemplateResponse("index1.html", {"request": request, "events": events})
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Failed to fetch events from Java API")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
