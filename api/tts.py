from gtts import gTTS
from io import BytesIO

def handler(request):
    text = request.args.get("text", "")

    if not text:
        return {
            "status": 400,
            "body": "Text is required"
        }

    mp3_bytes = BytesIO()
    tts = gTTS(text=text, lang="id")
    tts.write_to_fp(mp3_bytes)
    mp3_bytes.seek(0)

    return {
        "status": 200,
        "headers": {
            "Content-Type": "audio/mpeg",
            "Content-Disposition": "attachment; filename=tts.mp3"
        },
        "body": mp3_bytes.read()
    }
