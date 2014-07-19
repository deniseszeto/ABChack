import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ["POST"])
def submit_form():
    if request.method == 'POST':
        time = request.form['time']
        genre = request.form['genre']

        # figure out what song to play
        #change html so that the song is played
        return render_template('index.html', time = time, genre = genre, song_id = "12345678", play = "true")
    

@app.route('/')
def at_first():
    return render_template('index.html', time = "", genre = "", song_id = "0", play = "false")