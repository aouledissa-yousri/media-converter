

export class MediaPayloadHelper {

    public static createFormDataImagePayload(file: File) {
        const formData = new FormData()
        formData.append("image", file)
        return formData
    }

    public static createFormDataAudioPayload(file: File) {
        const formData = new FormData()
        formData.append("audio", file)
        return formData
    }

    public static createFormDataVideoPayload(file: File) {
        const formData = new FormData()
        formData.append("video", file)
        return formData
    }

    public static createFormDataVideoAudioConversionPayload(file: File, outputFormat: string){
        const formData = new FormData()
        formData.append("outputFormat", outputFormat)
        formData.append("video", file)

        return formData

    }

    
}