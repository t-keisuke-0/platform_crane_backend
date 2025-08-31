import os
if os.environ.get("ENV", "local") == "local":
    from dotenv import load_dotenv
    load_dotenv()
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_ORIGINS", "")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def hello():
    return "Hello, FastAPI!"

@app.get("/api/greet")
def greet(name: str = "World"):
    return {"message": f"Hello, {name}!"}

@app.post("/api/echo")
async def echo(request: Request):
    data = await request.json()
    return {"you_sent": data}
