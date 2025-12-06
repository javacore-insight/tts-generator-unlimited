from gtts import gTTS
from io import BytesIO

def handler(request):
    text = request.args.get("text", "")
    if not text:
        return {"status": 400, "body": "Error: missing text"}

    buf = BytesIO()
    gTTS(text=text, lang='id').write_to_fp(buf)
    mp3_data = buf.getvalue()

    return {
        "status": 200,
        "headers": {
            "Content-Type": "audio/mpeg",
            "Content-Disposition": "attachment; filename=tts.mp3"
        },
        "body": mp3_data
    }
