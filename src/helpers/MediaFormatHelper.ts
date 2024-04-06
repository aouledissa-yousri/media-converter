


export class MediaFormatHelper {

    private static readonly formats = {
        image: ["jpg", "png", "webp", "svg"],
        audio: ["mp3", "ogg", "m4a", "wav"],
        video: ["mp4", "avi", "flv", "webm", "mov"]
    }

    public static filterFormats(filename: string) {
        const extension = MediaFormatHelper.getFileExtension(filename)
        const selectedFormats = this.getFormatType(extension)

        return selectedFormats.filter((format) => format !== extension)
        
    }

    public static getFileExtension(filename: string) {
        return filename.split(".")[1]
    }

    public static getFileName(filename:string){
        return filename.split(".")[0]
    }

    private static getFormatType(extension: string) {
        if(this.formats.image.indexOf(extension) !== -1) return this.formats.image
        else if(this.formats.audio.indexOf(extension) !== -1) return this.formats.audio
        else if(this.formats.video.indexOf(extension) !== -1) return [...this.formats.video, ...this.formats.audio]

        return []
    }
}