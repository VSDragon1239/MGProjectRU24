from vosk import Model, KaldiRecognizer
from flask import Flask, request, jsonify
import wave
import io

from RecognizingRU24.Project.settings import *


app = Flask(__name__)

model = Model(str(HIGH_MODEL_PATH))


@app.route("/recognize", methods=["POST"])
def recognize():
    try:
        audio_data = request.data  # Это raw PCM audio 16-bit mono 16000Hz

        # Проверка: достаточно ли данных
        if len(audio_data) < 4000:
            return jsonify({"error": "Слишком мало данных для распознавания"}), 400

        rec = KaldiRecognizer(model, 16000)
        rec.SetWords(True)  # Показывает точные слова (необязательно)

        # Обработка поступивших данных в чанках
        buffer = io.BytesIO(audio_data)
        while True:
            chunk = buffer.read(4000)
            if len(chunk) == 0:
                break
            rec.AcceptWaveform(chunk)

        result = rec.FinalResult()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def runserver():
    app.run(host="0.0.0.0", port=5000)
