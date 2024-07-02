import axios from "axios";

export interface fineTuneType {
    prompt?: string,
    maxToken?: number,
    temperature?: number,
    topP?: number,
    maxCharacters?: number,
    eroor: string
}


export async function getfineTune(): Promise<fineTuneType> {
    try {
        const response = await axios.get("/getFineTune");
        return response.data;
    } catch (error) {
        console.error(error);
        return { prompt: "", maxToken: 0, temperature: 0, topP: 0, maxCharacters: 0, eroor: "Error: " + error };
    }
}

export async function setfineTune() {
    try {
        const response = await axios.get("/getFineTune");

        return response.data?.message;
    } catch (error) {
        console.error(error);
        return "Error: " + error;
    }
}
