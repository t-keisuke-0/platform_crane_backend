import os
import sys
import importlib
import pkgutil
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.conf as conf

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=conf.cors_options,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

sys.path.append(os.path.join(Path(__file__).parent))

routers_dir = os.path.join(Path(__file__).parent, "routers")
for _, name, ispkg in pkgutil.iter_modules([routers_dir], "routers."):
    if ispkg or name.startswith("_"):
        continue
    module = importlib.import_module(name)
    if hasattr(module, "router"):
        app.include_router(getattr(module, "router"), prefix="/api")
