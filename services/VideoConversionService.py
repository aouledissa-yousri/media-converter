from fastapi import UploadFile
from fastapi.responses import FileResponse
from helpers import MediaHelper

class VideoConversionService:

    # avi conversion
    @staticmethod
    async def convertAVItoFLV(video: UploadFile):

        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/avi_flv_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.flv", f"converted-files/{MediaHelper.getMediaName(video)}.flv")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.flv", 
            filename=MediaHelper.getMediaName(video)+".flv", 
            media_type="application/octet-stream"
        ) 
    

    @staticmethod
    async def convertAVItoMOV(video: UploadFile):

        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/avi_mov_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.mov", f"converted-files/{MediaHelper.getMediaName(video)}.mov")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.mov", 
            filename=MediaHelper.getMediaName(video)+".mov", 
            media_type="application/octet-stream"
        ) 
    

    @staticmethod
    async def convertAVItoMP4(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/avi_mp4_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.mp4", f"converted-files/{MediaHelper.getMediaName(video)}.mp4")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.mp4", 
            filename=MediaHelper.getMediaName(video)+".mp4", 
            media_type="application/octet-stream"
        ) 
    

    @staticmethod
    async def convertAVItoWEBM(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/avi_webm_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.webm", f"converted-files/{MediaHelper.getMediaName(video)}.webm")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.webm", 
            filename=MediaHelper.getMediaName(video)+".webm", 
            media_type="application/octet-stream"
        ) 
    











    # flv conversion
    @staticmethod
    async def convertFLVtoAVI(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/flv_avi_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.avi", f"converted-files/{MediaHelper.getMediaName(video)}.avi")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.avi", 
            filename=MediaHelper.getMediaName(video)+".avi", 
            media_type="application/octet-stream"
        ) 
    

    @staticmethod
    async def convertFLVtoMOV(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/flv_mov_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.mov", f"converted-files/{MediaHelper.getMediaName(video)}.mov")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.mov", 
            filename=MediaHelper.getMediaName(video)+".mov", 
            media_type="application/octet-stream"
        )
    

    @staticmethod
    async def convertFLVtoMP4(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/flv_mp4_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.mp4", f"converted-files/{MediaHelper.getMediaName(video)}.mp4")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.mp4", 
            filename=MediaHelper.getMediaName(video)+".mp4", 
            media_type="application/octet-stream"
        )
    

    @staticmethod
    async def convertFLVtoWEBM(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/flv_webm_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.webm", f"converted-files/{MediaHelper.getMediaName(video)}.webm")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.webm", 
            filename=MediaHelper.getMediaName(video)+".webm", 
            media_type="application/octet-stream"
        )
    









    # mov conversion
    @staticmethod
    async def convertMOVtoAVI(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/mov_avi_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.avi", f"converted-files/{MediaHelper.getMediaName(video)}.avi")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.avi", 
            filename=MediaHelper.getMediaName(video)+".avi", 
            media_type="application/octet-stream"
        )
    

    @staticmethod
    async def convertMOVtoFLV(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/mov_flv_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.flv", f"converted-files/{MediaHelper.getMediaName(video)}.flv")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.flv", 
            filename=MediaHelper.getMediaName(video)+".flv", 
            media_type="application/octet-stream"
        )
    

    @staticmethod
    async def convertMOVtoMP4(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/mov_mp4_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.mp4", f"converted-files/{MediaHelper.getMediaName(video)}.mp4")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.mp4", 
            filename=MediaHelper.getMediaName(video)+".mp4", 
            media_type="application/octet-stream"
        )
    

    @staticmethod
    async def convertMOVtoWEBM(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/mov_webm_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.webm", f"converted-files/{MediaHelper.getMediaName(video)}.webm")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.webm", 
            filename=MediaHelper.getMediaName(video)+".webm", 
            media_type="application/octet-stream"
        )
    












    # mp4 conversion
    @staticmethod
    async def convertMP4toAVI(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/mp4_avi_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.avi", f"converted-files/{MediaHelper.getMediaName(video)}.avi")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.avi", 
            filename=MediaHelper.getMediaName(video)+".avi", 
            media_type="application/octet-stream"
        )
    

    @staticmethod
    async def convertMP4toFLV(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/mp4_flv_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.flv", f"converted-files/{MediaHelper.getMediaName(video)}.flv")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.flv", 
            filename=MediaHelper.getMediaName(video)+".flv", 
            media_type="application/octet-stream"
        )
    

    @staticmethod
    async def convertMP4toMOV(video: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/mp4_mov_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.mov", f"converted-files/{MediaHelper.getMediaName(video)}.mov")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.mov", 
            filename=MediaHelper.getMediaName(video)+".mov", 
            media_type="application/octet-stream"
        )
    

    @staticmethod
    async def convertMP4toWEBM(video: UploadFile):
         
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/mp4_webm_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.webm", f"converted-files/{MediaHelper.getMediaName(video)}.webm")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.webm", 
            filename=MediaHelper.getMediaName(video)+".webm", 
            media_type="application/octet-stream"
        )
    










    # webm conversion
    @staticmethod
    async def convertWEBMtoAVI(video: UploadFile):
         
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/webm_avi_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.avi", f"converted-files/{MediaHelper.getMediaName(video)}.avi")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.avi", 
            filename=MediaHelper.getMediaName(video)+".avi", 
            media_type="application/octet-stream"
        )
    

    @staticmethod
    async def convertWEBMtoFLV(video: UploadFile):
         
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/webm_flv_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.flv", f"converted-files/{MediaHelper.getMediaName(video)}.flv")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.flv", 
            filename=MediaHelper.getMediaName(video)+".flv", 
            media_type="application/octet-stream"
        )
    

    @staticmethod
    async def convertWEBMtoMOV(video: UploadFile):
         
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/webm_mov_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.mov", f"converted-files/{MediaHelper.getMediaName(video)}.mov")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.mov", 
            filename=MediaHelper.getMediaName(video)+".mov", 
            media_type="application/octet-stream"
        )
    

    @staticmethod
    async def convertWEBMtoMP4(video: UploadFile):
         
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/webm_mp4_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.mp4", f"converted-files/{MediaHelper.getMediaName(video)}.mp4")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.mp4", 
            filename=MediaHelper.getMediaName(video)+".mp4", 
            media_type="application/octet-stream"
        )

    #convert to audio
    @staticmethod
    async def convertToAudio(video: UploadFile, outputFormat: str):

        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(video)
        MediaHelper.runMediaConversionProcess("conversion_processes/video_audio_conversion", [destinationPath, outputFormat])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(video)}.{outputFormat}", f"converted-files/{MediaHelper.getMediaName(video)}.{outputFormat}")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(video)}.{outputFormat}", 
            filename=MediaHelper.getMediaName(video)+f".{outputFormat}", 
            media_type="application/octet-stream"
        )