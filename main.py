from fastapi import FastAPI
from settings import apps
from fastapi.middleware.cors import CORSMiddleware
from settings import origins


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

for route, subApp in apps.items(): 
    app.include_router(subApp, prefix=f"/{route}")