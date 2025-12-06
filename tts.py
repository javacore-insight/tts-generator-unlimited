from gtts import gTTS
from flask import Flask, request, send_file
import uuid
import os

app = Flask(__name__)

@app.route('/api/tts')
def generate_tts():
    text = request.args.get("text", "")

    if not text:
        return {"error": "Text is required"}, 400

    # generate file name unik
    filename = f"{uuid.uuid4()}.mp3"

    # generate audio
    tts = gTTS(text=text, lang='id')
    tts.save(filename)

    # kirim hasil ke user (download)
    response = send_file(
        filename,
        mimetype="audio/mpeg",
        as_attachment=True,
        download_name="tts.mp3"
    )

    # hapus file setelah dikirim (supaya tidak menumpuk di server)
    @response.call_on_close
    def cleanup():
        try:
            os.remove(filename)
        except:
            pass

    return response