import axios from "axios";

export interface propType { userId: string, prompt: string };


export default async function subMitAndfetchResponse({ userId, prompt }: propType) {
    try {
        const data = { userId, prompt };
        const response = await axios.post("/chat", data);

        return response.data?.message;
    } catch (error) {
        console.error(error);
        return "Error: " + error;
    }
}
