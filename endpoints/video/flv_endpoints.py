from fastapi import APIRouter, UploadFile

app = APIRouter()


@app.post("/avi/")
async def convertToFLV(video: UploadFile):

    return "hello world"


@app.post("/mov/")
async def convertToMOV(video: UploadFile):

    return "hello world"

@app.post("/mp4/")
async def convertToMP4(video: UploadFile):

    return "hello world"


@app.post("/webm/")
async def convertToWEBP(video: UploadFile):

    return "hello world"