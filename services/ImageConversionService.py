from fastapi import UploadFile
from helpers import MediaHelper
from fastapi.responses import FileResponse

import asyncio



class ImageConversionService: 

    #jpg conversions
    @staticmethod
    async def convertJPGtoPNG(image: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/jpg_png_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.png", f"converted-files/{MediaHelper.getMediaName(image)}.png")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.png", 
            filename=MediaHelper.getMediaName(image)+".png", 
            media_type="application/octet-stream"
        ) 
    

    @staticmethod
    async def convertJPGtoSVG(image: UploadFile):
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/jpg_svg_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.svg", f"converted-files/{MediaHelper.getMediaName(image)}.svg")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.svg", 
            filename=MediaHelper.getMediaName(image)+".svg", 
            media_type="application/octet-stream"
        )  
    

    @staticmethod
    async def convertJPGtoWEBP(image: UploadFile):
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/jpg_webp_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.webp", f"converted-files/{MediaHelper.getMediaName(image)}.webp")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.webp", 
            filename=MediaHelper.getMediaName(image)+".webp", 
            media_type="application/octet-stream"
        )  
    

    #png conversions
    @staticmethod
    async def convertPNGtoJPG(image: UploadFile):
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/png_jpg_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.jpg", f"converted-files/{MediaHelper.getMediaName(image)}.jpg")
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.jpg", 
            filename=MediaHelper.getMediaName(image)+".jpg", 
            media_type="application/octet-stream"
        )
    
    @staticmethod
    async def convertPNGtoSVG(image: UploadFile):
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/png_svg_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.svg", f"converted-files/{MediaHelper.getMediaName(image)}.svg")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.svg", 
            filename=MediaHelper.getMediaName(image)+".svg", 
            media_type="application/octet-stream"
        )  
    
    @staticmethod
    async def convertPNGtoWEBP(image: UploadFile):
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/png_webp_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.webp", f"converted-files/{MediaHelper.getMediaName(image)}.webp")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.webp", 
            filename=MediaHelper.getMediaName(image)+".webp", 
            media_type="application/octet-stream"
        )  
    

    #svg conversions
    @staticmethod
    async def convertSVGtoJPG(image: UploadFile):
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/svg_jpg_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.jpg", f"converted-files/{MediaHelper.getMediaName(image)}.jpg")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.jpg", 
            filename=MediaHelper.getMediaName(image)+".jpg", 
            media_type="application/octet-stream"
        )  
    
    @staticmethod
    async def convertSVGtoPNG(image: UploadFile):
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/svg_png_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.png", f"converted-files/{MediaHelper.getMediaName(image)}.png")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.png", 
            filename=MediaHelper.getMediaName(image)+".png", 
            media_type="application/octet-stream"
        )  
    
    @staticmethod
    async def convertSVGtoWEBP(image: UploadFile):
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/svg_webp_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.webp", f"converted-files/{MediaHelper.getMediaName(image)}.webp")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.webp", 
            filename=MediaHelper.getMediaName(image)+".webp", 
            media_type="application/octet-stream"
        )  
    

    #webp conversions
    @staticmethod
    async def convertWEBPtoJPG(image: UploadFile):
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/webp_jpg_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.jpg", f"converted-files/{MediaHelper.getMediaName(image)}.jpg")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.jpg", 
            filename=MediaHelper.getMediaName(image)+".jpg", 
            media_type="application/octet-stream"
        )  
    
    @staticmethod
    async def convertWEBPtoPNG(image: UploadFile):
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/webp_png_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.png", f"converted-files/{MediaHelper.getMediaName(image)}.png")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.png", 
            filename=MediaHelper.getMediaName(image)+".png", 
            media_type="application/octet-stream"
        )  
    
    @staticmethod
    async def convertWEBPtoSVG(image: UploadFile):
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(image)
        MediaHelper.runMediaConversionProcess("conversion_processes/webp_svg_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(image)}.svg", f"converted-files/{MediaHelper.getMediaName(image)}.svg")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(image)}.svg", 
            filename=MediaHelper.getMediaName(image)+".svg", 
            media_type="application/octet-stream"
        )  