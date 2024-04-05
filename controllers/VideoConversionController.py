from fastapi import UploadFile
from services import VideoConversionService


class VideoConversionController:
    
    # avi conversion
    @staticmethod
    def convertAVItoFLV(video: UploadFile):
        return VideoConversionService.convertAVItoFLV(video)

    @staticmethod
    def convertAVItoMOV(video: UploadFile):
        return VideoConversionService.convertAVItoMOV(video)

    @staticmethod
    def convertAVItoMP4(video: UploadFile):
        return VideoConversionService.convertAVItoMP4(video)

    @staticmethod
    def convertAVItoWEBM(video: UploadFile):
        return VideoConversionService.convertAVItoWEBM(video)
    





    # flv conversion
    @staticmethod
    def convertFLVtoAVI(video: UploadFile):
        return VideoConversionService.convertFLVtoAVI(video)

    @staticmethod
    def convertFLVtoMOV(video: UploadFile):
        return VideoConversionService.convertFLVtoMOV(video)

    @staticmethod
    def convertFLVtoMP4(video: UploadFile):
        return VideoConversionService.convertFLVtoMP4(video)

    @staticmethod
    def convertFLVtoWEBM(video: UploadFile):
        return VideoConversionService.convertFLVtoWEBM(video)
    








    # mov conversion
    @staticmethod
    def convertMOVtoAVI(video: UploadFile):
        return VideoConversionService.convertMOVtoAVI(video)

    @staticmethod
    def convertMOVtoFLV(video: UploadFile):
        return VideoConversionService.convertMOVtoFLV(video)

    @staticmethod
    def convertMOVtoMP4(video: UploadFile):
        return VideoConversionService.convertMOVtoMP4(video)

    @staticmethod
    def convertMOVtoWEBM(video: UploadFile):
        return VideoConversionService.convertMOVtoWEBM(video)








    # mp4 conversion
    @staticmethod
    def convertMP4toAVI(video: UploadFile):
        return VideoConversionService.convertMP4toAVI(video)

    @staticmethod
    def convertMP4toFLV(video: UploadFile):
        return VideoConversionService.convertMP4toFLV(video)

    @staticmethod
    def convertMP4toMOV(video: UploadFile):
        return VideoConversionService.convertMP4toMOV(video)

    @staticmethod
    def convertMP4toWEBM(video: UploadFile):
        return VideoConversionService.convertMP4toWEBM(video)
    






    

    # webm conversion
    @staticmethod
    def convertWEBMtoAVI(video: UploadFile):
        return VideoConversionService.convertWEBMtoAVI(video)

    @staticmethod
    def convertWEBMtoFLV(video: UploadFile):
        return VideoConversionService.convertWEBMtoFLV(video)

    @staticmethod
    def convertWEBMtoMOV(video: UploadFile):
        return VideoConversionService.convertWEBMtoMOV(video)

    @staticmethod
    def convertWEBMtoMP4(video: UploadFile):
        return VideoConversionService.convertWEBMtoMP4(video)

    
    #convert to audio
    @staticmethod
    def convertToAudio(video: UploadFile, outputFormat: str):
        return VideoConversionService.convertToAudio(video, outputFormat)
