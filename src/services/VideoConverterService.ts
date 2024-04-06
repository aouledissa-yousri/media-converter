import { API_URL } from "../global";
import { MediaPayloadHelper } from "../helpers/MediaPayloadHelper";
import { HttpRequestHelper } from "../helpers/HttpRequestHelper";


export class VideoConverterService {

    // AVI Conversion
    public static async convertAVItoFLV(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/avi/flv/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertAVItoMOV(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/avi/mov/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertAVItoMP4(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/avi/mp4/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertAVItoWEBM(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/avi/webm/", MediaPayloadHelper.createFormDataImagePayload(video));
    }







    // FLV Conversion
    public static async convertFLVtoAVI(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/flv/avi/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertFLVtoMOV(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/flv/mov/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertFLVtoMP4(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/flv/mp4/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertFLVtoWEBM(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/flv/webm/", MediaPayloadHelper.createFormDataImagePayload(video));
    }








    // MOV Conversion
    public static async convertMOVtoAVI(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/mov/avi/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertMOVtoFLV(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/mov/flv/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertMOVtoMP4(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/mov/mp4/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertMOVtoWEBM(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/mov/webm/", MediaPayloadHelper.createFormDataImagePayload(video));
    }




    

    // MP4 Conversion
    public static async convertMP4toAVI(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/mp4/avi/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertMP4toFLV(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/mp4/flv/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertMP4toMOV(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/mp4/mov/", MediaPayloadHelper.createFormDataImagePayload(video));
    }

    public static async convertMP4toWEBM(video: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL + "/mp4/webm/", MediaPayloadHelper.createFormDataImagePayload(video));
    }
}