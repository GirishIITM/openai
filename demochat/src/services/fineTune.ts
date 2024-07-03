import axios from "axios";
import toast from "react-hot-toast";

export interface fineTuneType {
    prompt?: string,
    maxToken?: number,
    temperature?: number,
    maxCharacters?: number,
    rate?: {
        [key: string]: number
    },
    eroor: string
}


export async function getfineTune(): Promise<fineTuneType> {
    try {
        const response = await axios.get("/getFineTune");
        return response.data;
    } catch (error) {
        console.error(error);
        toast.error("Error: " + error);
        return { prompt: "", maxToken: 0, temperature: 0, maxCharacters: 0, eroor: "Error: " + error };
    }
}

export async function setfineTune(details: fineTuneType): Promise<string> {
    try {
        const response = await axios.post("/setFineTune", details);
        toast.success("Details updated successfully");
        return response.data?.message;
    } catch (error) {
        console.error(error);
        toast.error("Failed to fetch details: " + error);
        return "Error: " + error;
    }
}
