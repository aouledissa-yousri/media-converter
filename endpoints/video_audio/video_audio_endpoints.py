from fastapi import APIRouter, UploadFile


app = APIRouter()

@app.post("/")
async def convertToAudio(video: UploadFile):

    return "hello world"

