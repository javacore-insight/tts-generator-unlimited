from gtts import gTTS
from io import BytesIO

def handler(request):
    text = request.args.get("text", "")

    if not text:
        return {
            "status": 400,
            "body": "Text is required"
        }

    # Generate MP3 in memory
    buf = BytesIO()
    tts = gTTS(text=text, lang="id")
    tts.write_to_fp(buf)
    audio_bytes = buf.getvalue()

    return {
        "status": 200,
        "headers": {
            "Content-Type": "audio/mpeg",
            "Content-Disposition": "attachment; filename=tts.mp3"
        },
        "body": audio_bytes
    }
