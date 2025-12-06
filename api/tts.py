from gtts import gTTS
import uuid
import os

def handler(request):
    # Get text from query
    text = request.query.get("text", "")

    if not text:
        return {
            "status": 400,
            "body": "Error: text is required."
        }

    filename = f"/tmp/{uuid.uuid4()}.mp3"

    # Generate audio
    tts = gTTS(text, lang="id")
    tts.save(filename)

    # Read file
    with open(filename, "rb") as f:
        audio_data = f.read()

    # Delete temp file
    os.remove(filename)

    return {
        "status": 200,
        "headers": {
            "Content-Type": "audio/mpeg"
        },
        "body": audio_data,
        "encoding": "binary"
    }
