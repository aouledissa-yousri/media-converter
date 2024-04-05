from fastapi import APIRouter, UploadFile

app = APIRouter()


@app.post("/m4a/")
async def convertToM4A(audio: UploadFile):

    return "hello world"


@app.post("/mp3/")
async def convertToMP3(audio: UploadFile):

    return "hello world"

@app.post("/ogg/")
async def convertToOGG(audio: UploadFile):

    return "hello world"