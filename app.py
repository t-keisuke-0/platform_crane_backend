from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://platform-crane-frontend.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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
