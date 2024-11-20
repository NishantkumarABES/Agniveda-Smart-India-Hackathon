from flask import Flask, redirect, url_for, render_template, request
from gtts import gTTS
import pygame
import gunicorn
import io

count = 0

def speak(text):
    sound = gTTS(text=text, lang='hi')
    audio_data = io.BytesIO()
    sound.write_to_fp(audio_data)
    audio_data.seek(0)  
    pygame.mixer.init()
    pygame.mixer.music.load(audio_data)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


app = Flask(__name__, template_folder="template", static_folder="static")


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/blog_page")
def blog_page():
    return render_template('blog_page.html')

@app.route("/chatbot")
def veda():
    return render_template('chatbot.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    speak(str(msg))
    Input = msg
    text = get_chat_response(Input)
    speak(text)
    return text

@app.route("/practitioner_login")
def practitioner_login():
    return render_template('practitioner_login.html')

@app.route("/practitioner")
def practitioner_page():
    return render_template('video_page.html')

def get_chat_response(text):
    response_text = str(answerMe(text))
    return response_text

if __name__ == "__main__":
    app.run(debug=True)
    # gunicorn.run(app, host="0.0.0.0", port=8000)

