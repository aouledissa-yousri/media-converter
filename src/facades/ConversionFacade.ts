import { MediaFormatHelper } from "../helpers/MediaFormatHelper"
import { AudioConverterService } from "../services/AudioConverterService"
import { ImageConverterService } from "../services/ImageConverterService"
import { VideoConverterService } from "../services/VideoConverterService"

export class ConversionFacade {

  public static async convert(file: File, filename: string, outputFormat: string) {
    const extension = MediaFormatHelper.getFileExtension(filename)

    switch (extension) {

      case "jpg":
        switch (outputFormat) {

          case "png":
            return ImageConverterService.convertJPGtoPNG(file)

          case "webp":
            return ImageConverterService.convertJPGtoWEBP(file)

          case "svg":
            return ImageConverterService.convertJPGtoSVG(file)

          default:
            throw new Error(
              `Conversion from JPG to ${outputFormat} is not supported.`
            )

        }

      case "png":
        switch (outputFormat) {

          case "jpg":
            return ImageConverterService.convertPNGtoJPG(file)

          case "webp":
            return ImageConverterService.convertPNGtoWEBP(file)

          case "svg":
            return ImageConverterService.convertPNGtoSVG(file)

          default:
            throw new Error(
              `Conversion from PNG to ${outputFormat} is not supported.`
            )

        }

      case "webp":

        switch (outputFormat) {
          case "jpg":
            return ImageConverterService.convertWEBPtoJPG(file)

          case "png":
            return ImageConverterService.convertWEBPtoPNG(file)

          case "svg":
            return ImageConverterService.convertWEBPtoSVG(file)

          default:
            throw new Error(
              `Conversion from WEBP to ${outputFormat} is not supported.`
            )
        }

      case "svg":
        switch (outputFormat) {

          case "jpg":
            return ImageConverterService.convertSVGtoJPG(file)

          case "png":
            return ImageConverterService.convertSVGtoPNG(file)

          case "webp":
            return ImageConverterService.convertSVGtoWEBP(file)

          default:
            throw new Error(
              `Conversion from SVG to ${outputFormat} is not supported.`
            )
        }

      case "wav":
        switch (outputFormat) {

          case "mp3":
            return AudioConverterService.convertWAVtoMP3(file)

          case "m4a":
            return AudioConverterService.convertWAVtoM4A(file)

          case "ogg":
            return AudioConverterService.convertWAVtoOGG(file)

          default:
            throw new Error(
              `Conversion from WAV to ${outputFormat} is not supported.`
            )
        }
        
      case "mp3":
        switch (outputFormat) {
          case "wav":
            return AudioConverterService.convertMP3toWAV(file)

          case "m4a":
            return AudioConverterService.convertMP3toM4A(file)

          case "ogg":
            return AudioConverterService.convertMP3toOGG(file)

          default:
            throw new Error(
              `Conversion from MP3 to ${outputFormat} is not supported.`
            )
        }

      case "m4a":
        switch (outputFormat) {

          case "wav":
            return AudioConverterService.convertM4AtoWAV(file)

          case "mp3":
            return AudioConverterService.convertM4AtoMP3(file)

          case "ogg":
            return AudioConverterService.convertM4AtoOGG(file)

          default:
            throw new Error(
              `Conversion from M4A to ${outputFormat} is not supported.`
            )
        }

      case "ogg":
        switch (outputFormat) {
          case "wav":
            return AudioConverterService.convertOGGtoWAV(file)

          case "mp3":
            return AudioConverterService.convertOGGtoMP3(file)

          case "m4a":
            return AudioConverterService.convertOGGtoM4A(file)

          default:
            throw new Error(
              `Conversion from OGG to ${outputFormat} is not supported.`
            )
        }

      case "mp4":
        switch (outputFormat) {

          case "avi":
            return VideoConverterService.convertMP4toAVI(file)

          case "flv":
            return VideoConverterService.convertMP4toFLV(file)

          case "mov":
            return VideoConverterService.convertMP4toMOV(file)

          case "webm":
            return VideoConverterService.convertMP4toWEBM(file)

          default:
            return VideoConverterService.convertVideoToAudio(file, outputFormat)
        }

      case "avi":
        switch (outputFormat) {

          case "mp4":
            return VideoConverterService.convertAVItoMP4(file)

          case "flv":
            return VideoConverterService.convertAVItoFLV(file)

          case "mov":
            return VideoConverterService.convertAVItoMOV(file)

          case "webm":
            return VideoConverterService.convertAVItoWEBM(file)

          default:
            return VideoConverterService.convertVideoToAudio(file, outputFormat)
        }


      case "flv":
        switch (outputFormat) {
          case "mp4":
            return VideoConverterService.convertFLVtoMP4(file)

          case "avi":
            return VideoConverterService.convertFLVtoAVI(file)

          case "mov":
            return VideoConverterService.convertFLVtoMOV(file)

          case "webm":
            return VideoConverterService.convertFLVtoWEBM(file)

          default:
            return VideoConverterService.convertVideoToAudio(file, outputFormat)
        }


      case "mov":
        switch (outputFormat) {

          case "mp4":
            return VideoConverterService.convertMOVtoMP4(file)

          case "avi":
            return VideoConverterService.convertMOVtoAVI(file)

          case "flv":
            return VideoConverterService.convertMOVtoFLV(file)

          case "webm":
            return VideoConverterService.convertMOVtoWEBM(file)

          default:
            return VideoConverterService.convertVideoToAudio(file, outputFormat)
        }


      case "webm":
        switch (outputFormat) {
          case "mp4":
            return VideoConverterService.convertWEBMtoMP4(file)

          case "avi":
            return VideoConverterService.convertWEBMtoAVI(file)

          case "flv":
            return VideoConverterService.convertWEBMtoFLV(file)

          case "mov":
            return VideoConverterService.convertWEBMtoMOV(file)

          default:
            return VideoConverterService.convertVideoToAudio(file, outputFormat)
        }

      default:
        throw new Error(`Input format ${extension} is not supported.`)
    }
  }
}
