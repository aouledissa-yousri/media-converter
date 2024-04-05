from services import AudioConversionService
from fastapi import UploadFile

class AudioConversionController: 
    

    #m4a conversion

    @staticmethod 
    def convertM4AtoMP3(audio: UploadFile):
        return AudioConversionService.convertM4AtoMP3(audio)
    
    @staticmethod 
    def convertM4AtoOGG(audio: UploadFile):
        return AudioConversionService.convertM4AtoOGG(audio)
    
    @staticmethod 
    def convertM4AtoWAV(audio: UploadFile):
        return AudioConversionService.convertM4AtoWAV(audio)
    

    #mp3 conversion

    @staticmethod 
    def convertMP3toM4A(audio: UploadFile):
        return AudioConversionService.convertMP3toM4A(audio)
    
    @staticmethod 
    def convertMP3toOGG(audio: UploadFile):
        return AudioConversionService.convertMP3toM4A(audio)
    
    @staticmethod 
    def convertMP3toWAV(audio: UploadFile):
        return AudioConversionService.convertMP3toWAV(audio)
    



    #ogg conversion

    @staticmethod 
    def convertOGGtoM4A(audio: UploadFile):
        return AudioConversionService.convertOGGtoM4A(audio)
    
    @staticmethod 
    def convertOGGtoMP3(audio: UploadFile):
        return AudioConversionService.convertOGGtoMP3(audio)
    
    @staticmethod 
    def convertOGGtoWAV(audio: UploadFile):
        return AudioConversionService.convertOGGtoWAV(audio)
    

    

    #wav conversion
    @staticmethod 
    def convertWAVtoM4A(audio: UploadFile):
        return AudioConversionService.convertWAVtoM4A(audio)
    
    @staticmethod 
    def convertWAVtoMP3(audio: UploadFile):
        return AudioConversionService.convertWAVtoMP3(audio)
    
    @staticmethod 
    def convertWAVtoOGG(audio: UploadFile):
        return AudioConversionService.convertWAVtoOGG(audio)