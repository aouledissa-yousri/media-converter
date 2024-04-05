from fastapi import UploadFile
from fastapi.responses import FileResponse
from helpers import MediaHelper

class AudioConversionService: 
    

    #m4a conversion

    @staticmethod 
    async def convertM4AtoMP3(audio: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/m4a_mp3_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.mp3", f"converted-files/{MediaHelper.getMediaName(audio)}.mp3")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.mp3", 
            filename=MediaHelper.getMediaName(audio)+".mp3", 
            media_type="application/octet-stream"
        ) 
    
    @staticmethod 
    async def convertM4AtoOGG(audio: UploadFile):

        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/mp3_m4a_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.ogg", f"converted-files/{MediaHelper.getMediaName(audio)}.ogg")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.ogg", 
            filename=MediaHelper.getMediaName(audio)+".ogg", 
            media_type="application/octet-stream"
        ) 
    
    @staticmethod 
    async def convertM4AtoWAV(audio: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/m4a_wav_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.wav", f"converted-files/{MediaHelper.getMediaName(audio)}.wav")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.wav", 
            filename=MediaHelper.getMediaName(audio)+".wav", 
            media_type="application/octet-stream"
        ) 
    

    #mp3 conversion

    @staticmethod 
    async def convertMP3toM4A(audio: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/mp3_m4a_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.m4a", f"converted-files/{MediaHelper.getMediaName(audio)}.m4a")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.m4a", 
            filename=MediaHelper.getMediaName(audio)+".m4a", 
            media_type="application/octet-stream"
        ) 
    
    @staticmethod 
    async def convertMP3toOGG(audio: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/mp3_m4a_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.ogg", f"converted-files/{MediaHelper.getMediaName(audio)}.ogg")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.ogg", 
            filename=MediaHelper.getMediaName(audio)+".ogg", 
            media_type="application/octet-stream"
        ) 
    
    @staticmethod 
    async def convertMP3toWAV(audio: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/m4a_wav_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.wav", f"converted-files/{MediaHelper.getMediaName(audio)}.wav")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.wav", 
            filename=MediaHelper.getMediaName(audio)+".wav", 
            media_type="application/octet-stream"
        ) 
    



    #ogg conversion

    @staticmethod 
    async def convertOGGtoM4A(audio: UploadFile):
        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/ogg_m4a_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.m4a", f"converted-files/{MediaHelper.getMediaName(audio)}.m4a")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.m4a", 
            filename=MediaHelper.getMediaName(audio)+".m4a", 
            media_type="application/octet-stream"
        ) 
    
    @staticmethod 
    async def convertOGGtoMP3(audio: UploadFile):
                
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/ogg_mp3_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.mp3", f"converted-files/{MediaHelper.getMediaName(audio)}.mp3")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.mp3", 
            filename=MediaHelper.getMediaName(audio)+".mp3", 
            media_type="application/octet-stream"
        )  
    
    @staticmethod 
    async def convertOGGtoWAV(audio: UploadFile):
                
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/ogg_wav_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.wav", f"converted-files/{MediaHelper.getMediaName(audio)}.wav")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.wav", 
            filename=MediaHelper.getMediaName(audio)+".wav", 
            media_type="application/octet-stream"
        )  
    

    

    #wav conversion
    @staticmethod 
    async def convertWAVtoM4A(audio: UploadFile):
                
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/wav_m4a_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.m4a", f"converted-files/{MediaHelper.getMediaName(audio)}.m4a")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.m4a", 
            filename=MediaHelper.getMediaName(audio)+".m4a", 
            media_type="application/octet-stream"
        )  
    
    @staticmethod 
    async def convertWAVtoMP3(audio: UploadFile):
                        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/wav_mp3_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.mp3", f"converted-files/{MediaHelper.getMediaName(audio)}.mp3")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.mp3", 
            filename=MediaHelper.getMediaName(audio)+".mp3", 
            media_type="application/octet-stream"
        )  
    
    @staticmethod 
    async def convertWAVtoOGG(audio: UploadFile):
                        
        MediaHelper.clearConvertedFilesCache()

        destinationPath = await MediaHelper.createTempFile(audio)
        MediaHelper.runMediaConversionProcess("conversion_processes/wav_ogg_conversion", [destinationPath])
        MediaHelper.transferMedia(f"{MediaHelper.getMediaName(audio)}.ogg", f"converted-files/{MediaHelper.getMediaName(audio)}.ogg")
        
        MediaHelper.clearUploadCache()

        return FileResponse(
            path=f"converted-files/{MediaHelper.getMediaName(audio)}.ogg", 
            filename=MediaHelper.getMediaName(audio)+".ogg", 
            media_type="application/octet-stream"
        )  
