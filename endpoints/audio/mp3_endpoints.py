from fastapi import APIRouter, UploadFile

app = APIRouter()


@app.post("/m4a/")
async def convertToM4A(audio: UploadFile):

    return "hello world"


@app.post("/ogg/")
async def convertToOGG(audio: UploadFile):

    return "hello world"

@app.post("/wav/")
async def convertToWAV(audio: UploadFile):

    return "hello world"