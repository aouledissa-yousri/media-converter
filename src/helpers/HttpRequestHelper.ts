import axios from "axios"

export class HttpRequestHelper {

    public static async sendFormDataPostRequest(url: string, payload: FormData) {
        try {
            const response = await axios.post(url, payload, {

                headers: {
                    'Content-Type': 'multipart/form-data',
                },

                responseType: 'blob', 
            });
            
            return response.data; 
        } catch (error) {
            console.error('File upload error:', error);
            throw error; 
        }
    }

}