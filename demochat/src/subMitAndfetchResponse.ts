import axios from "axios";

export interface propType { userId: string, prompt: string };

const backendUrl = "http://127.0.0.1:5000"

export default async function subMitAndfetchResponse({ userId, prompt }: propType) {
    try {
        const data = { userId, prompt };
        const response = await axios.post(backendUrl + "/chat", data);

        return response.data?.message;
    } catch (error) {
        console.error(error);
        return "Error: " + error;
    }
}
