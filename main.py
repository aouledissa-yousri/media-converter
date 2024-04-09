from fastapi import FastAPI, Request
from settings import apps
from fastapi.middleware.cors import CORSMiddleware
from settings import origins
from pyngrok import ngrok

import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Middleware to measure execution time
@app.middleware("http")
async def measure_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time : {execution_time} seconds")
    return response

for route, subApp in apps.items(): 
    app.include_router(subApp, prefix=f"/{route}")

public_url = ngrok.connect(addr="8000")
print("Public URL:", public_url)