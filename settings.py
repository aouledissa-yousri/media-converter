from endpoints.audio import *
from endpoints.image import *
from endpoints.video import *
from endpoints.video_audio import *


# Define allowed origins
origins = [
    "http://localhost:3000",
    # Add any other allowed origins here
]


apps = {
    "m4a": m4a, 
    "mp3": mp3, 
    "ogg": ogg, 
    "wav": wav, 
    "jpg": jpg, 
    "png": png, 
    "svg": svg, 
    "webp": webp, 
    "avi": avi, 
    "flv": flv, 
    "mov": mov, 
    "mp4": mp4, 
    "webm": webm, 
    "videoAudio": videoAudio
}