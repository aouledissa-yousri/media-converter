

export class MediaPayloadHelper {

    public static createFormDataImagePayload(file: File) {
        const formData = new FormData()
        formData.append("image", file)
        return formData
    }
}