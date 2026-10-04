from flask import Flask, render_template, request
from langdetect import detect, detect_langs
from langdetect.lang_detect_exception import LangDetectException

app = Flask(__name__)

LANGUAGE_NAMES = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "ru": "Russian",
    "ar": "Arabic",
    "hi": "Hindi",
    "te": "Telugu",
    "ta": "Tamil",
    "kn": "Kannada",
    "ml": "Malayalam",
    "bn": "Bengali",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-cn": "Chinese",
}


def detect_language(text):
    try:
        code = detect(text)
        probabilities = detect_langs(text)

        language = LANGUAGE_NAMES.get(code, code)

        confidence = 0
        for item in probabilities:
            if item.lang == code:
                confidence = round(item.prob * 100, 2)
                break

        return language, code, confidence

    except LangDetectException:
        return "Unable to detect", "-", 0


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    language = None
    code = None
    confidence = None

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if text:
            language, code, confidence = detect_language(text)

    return render_template(
        "index.html",
        text=text,
        language=language,
        code=code,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)
