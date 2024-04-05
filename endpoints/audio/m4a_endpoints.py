from fastapi import APIRouter, UploadFile

app = APIRouter()


@app.post("/mp3/")
async def convertToMP3(audio: UploadFile):

    return "hello world"


@app.post("/ogg/")
async def convertToOGG(audio: UploadFile):

    return "hello world"

@app.post("/wav/")
async def convertToWAV(audio: UploadFile):

    return "hello world"