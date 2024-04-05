from fastapi import APIRouter, UploadFile

app = APIRouter()


@app.post("/m4a/")
async def convertToM4a(audio: UploadFile):

    return "hello world"


@app.post("/mp3/")
async def convertToMP3(audio: UploadFile):

    return "hello world"

@app.post("/wav/")
async def convertToWAV(audio: UploadFile):

    return "hello world"