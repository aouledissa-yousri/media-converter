from services import ImageConversionService
from fastapi import UploadFile

class ImageConversionController :


    #jpg conversions
    @staticmethod
    def convertJPGtoPNG(image: UploadFile):
        return ImageConversionService.convertJPGtoPNG(image)
    

    @staticmethod
    def convertJPGtoSVG(image: UploadFile):
        return ImageConversionService.convertJPGtoSVG(image)
    

    @staticmethod
    def convertJPGtoWEBP(image: UploadFile):
        return ImageConversionService.convertJPGtoWEBP(image)
    

    #png conversions
    @staticmethod
    def convertPNGtoJPG(image: UploadFile):
        return ImageConversionService.convertPNGtoJPG(image)
    
    @staticmethod
    def convertPNGtoSVG(image: UploadFile):
        return ImageConversionService.convertPNGtoSVG(image)
    
    @staticmethod
    def convertPNGtoWEBP(image: UploadFile):
        return ImageConversionService.convertPNGtoWEBP(image)
    

    #svg conversions
    @staticmethod
    def convertSVGtoJPG(image: UploadFile):
        return ImageConversionService.convertSVGtoJPG(image)
    
    @staticmethod
    def convertSVGtoPNG(image: UploadFile):
        return ImageConversionService.convertSVGtoPNG(image)
    
    @staticmethod
    def convertSVGtoWEBP(image: UploadFile):
        return ImageConversionService.convertSVGtoWEBP(image)
    

    #webp conversions
    @staticmethod
    def convertWEBPtoJPG(image: UploadFile):
        return ImageConversionService.convertWEBPtoJPG(image)
    
    @staticmethod
    def convertWEBPtoPNG(image: UploadFile):
        return ImageConversionService.convertWEBPtoPNG(image)
    
    @staticmethod
    def convertWEBPtoSVG(image: UploadFile):
        return ImageConversionService.convertWEBPtoSVG(image)
