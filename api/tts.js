import { TextToSpeechClient } from "@google-cloud/text-to-speech";

export default async function handler(req, res) {
    const text = req.query.text || "";

    if (!text) {
        return res.status(400).send("Error: text is required.");
    }

    const client = new TextToSpeechClient({
        credentials: JSON.parse(process.env.GOOGLE_TTS_KEY)
    });

    const [response] = await client.synthesizeSpeech({
        input: { text },
        voice: { languageCode: "id-ID", name: "id-ID-Wavenet-A" },
        audioConfig: { audioEncoding: "MP3" }
    });

    res.setHeader("Content-Type", "audio/mpeg");
    res.send(Buffer.from(response.audioContent, "base64"));
}
