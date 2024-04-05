from pathlib import Path
from typing import List
from fastapi import UploadFile

import shutil
import os
import subprocess


class MediaHelper: 

    @staticmethod
    async def createTempFile(file: UploadFile):

        destinationPath = os.path.join(Path("uploads"), file.filename)

        # Open the destination file for writing
        with open(destinationPath, "wb+") as destination:
            shutil.copyfileobj(file.file, destination)
        
        return destinationPath
    
    @staticmethod
    def deleteTempFile(file: UploadFile):
        os.remove(os.path.join(Path("uploads"), file.filename))

    @staticmethod
    def runMediaConversionProcess(processPath: str, parameters: List[str]):
        subprocess.run([processPath] + parameters, check=True)

    @staticmethod  
    def transferMedia(sourcePath: str, destinationPath: str):
        shutil.move(sourcePath, destinationPath)
    
    @staticmethod
    def getMediaName(file: UploadFile):
        filename, extension = os.path.splitext(file.filename)
        return filename

    @staticmethod 
    def clearUploadCache():
        for filename in os.listdir("uploads"):
            if filename != ".gitkeep":
                os.remove(os.path.join("uploads", filename))

    

    @staticmethod
    def clearConvertedFilesCache():
        for filename in os.listdir("converted-files"):
            if filename != ".gitkeep":
                os.remove(os.path.join("converted-files", filename))