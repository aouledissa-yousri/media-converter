import { API_URL } from "../global";
import { MediaPayloadHelper } from "../helpers/MediaPayloadHelper";
import { HttpRequestHelper } from "../helpers/HttpRequestHelper";

export class AudioConverterService {

    // M4A Conversion
    public static async convertM4AtoMP3(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/m4a/mp3/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }

    public static async convertM4AtoOGG(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/m4a/ogg/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }

    public static async convertM4AtoWAV(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/m4a/wav/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }







    // MP3 Conversion
    public static async convertMP3toM4A(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/mp3/m4a/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }

    public static async convertMP3toOGG(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/mp3/ogg/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }

    public static async convertMP3toWAV(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/mp3/wav/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }








    // OGG Conversion
    public static async convertOGGtoM4A(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/ogg/m4a/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }

    public static async convertOGGtoMP3(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/ogg/mp3/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }

    public static async convertOGGtoWAV(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/ogg/wav/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }







    

    // WAV Conversion
    public static async convertWAVtoM4A(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/wav/m4a/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }

    public static async convertWAVtoMP3(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/wav/mp3/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }

    public static async convertWAVtoOGG(audio: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/wav/ogg/", MediaPayloadHelper.createFormDataImagePayload(audio));
    }


}