from fastapi import FastAPI
from settings import apps


app = FastAPI()

for route, subApp in apps.items(): 
    app.include_router(subApp, prefix=f"/{route}")