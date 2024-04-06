import { API_URL } from "../global";
import { MediaPayloadHelper } from "../helpers/MediaPayloadHelper";
import { HttpRequestHelper } from "../helpers/HttpRequestHelper";

export class ImageConverterService {


    // JPG Conversion

    public static async convertJPGtoPNG(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/jpg/png/", MediaPayloadHelper.createFormDataImagePayload(image))
    }

    public static async convertJPGtoSVG(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/jpg/svg/", MediaPayloadHelper.createFormDataImagePayload(image))
    }

    public static async convertJPGtoWEBP(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/jpg/webp/", MediaPayloadHelper.createFormDataImagePayload(image))
    }





    // PNG Conversion

    public static async convertPNGtoJPG(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/png/jpg/", MediaPayloadHelper.createFormDataImagePayload(image))
    }

    public static async convertPNGtoSVG(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/png/svg/", MediaPayloadHelper.createFormDataImagePayload(image))
    }

    public static async convertPNGtoWEBP(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/png/webp/", MediaPayloadHelper.createFormDataImagePayload(image))
    }




    // SVG Conversion

    public static async convertSVGtoJPG(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/svg/jpg/", MediaPayloadHelper.createFormDataImagePayload(image))
    }

    public static async convertSVGtoPNG(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/svg/png/", MediaPayloadHelper.createFormDataImagePayload(image))
    }

    public static async convertSVGtoWEBP(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/svg/webp/", MediaPayloadHelper.createFormDataImagePayload(image))
    }




    
    // WEBP Conversion

    public static async convertWEBPtoJPG(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/webp/jpg/", MediaPayloadHelper.createFormDataImagePayload(image))
    }

    public static async convertWEBPtoPNG(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/webp/png/", MediaPayloadHelper.createFormDataImagePayload(image))
    }

    public static async convertWEBPtoSVG(image: File): Promise<any> {
        return await HttpRequestHelper.sendFormDataPostRequest(API_URL+"/webp/svg/", MediaPayloadHelper.createFormDataImagePayload(image))
    }


}