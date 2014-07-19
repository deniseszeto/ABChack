import os
from flask import Flask, render_template
from urllib2 import urlopen
from xml.dom import minidom


app = Flask(__name__)

# @app.route('/', methods=["POST"])
# def submit_form(): 
#     time = request.form['time']
#     author = request.form['author']
#     genre = request.form['genre']
#     song_url = findSong(int(time), author, genre)
    # figure out what song to play
    #change html so that the song is played
    # return render_template('index.html', time = time, author = author, genre = genre, song_url = song_url, play = "true")
    

@app.route('/', methods = ["GET", "POST"])
def at_first():
# if request.method == "GET":
#     time = request.form['time']
#     author = request.form['author']
#     genre = request.form['genre']
#     song_url = findSong(int(time), author, genre)
# else:
    print dir(request)
    try:
        if request.method == "POST":
            time = request.form['time']
            author = request.form['author']
            genre = request.form['genre']
            song_url = findSong(int(time), author, genre)
            return render_template('index.html', time = time, author = author, genre = genre, song_url = song_url, play = "true")
        else:
            pass
    except:

        return render_template('index.html', time = "", author = "", genre = "", song_url = "0", play = "false")


# Assume *optional = (genre, author, etc..)
def findSong(duration, author=" ", genre="electronic"):
    CLIENT_ID = '93fbdae95f70cd94b70864746295c28f'
    
    url = "http://api.soundcloud.com/tracks?client_id=" + CLIENT_ID

    url += "&filter.duration="
    if duration < 2:
        url += "short"
    elif duration < 10:
        url += "medium"
    elif duration < 30:
        url += "long"
    else:
        url += "epic"
        
    url += "&genre=" + genre

    page = urlopen(url)
    xmldoc = minidom.parse(page)
    lengths = xmldoc.getElementsByTagName('duration')
    uris = []
    for el in xmldoc.getElementsByTagName('uri'):
        if "tracks" in el.firstChild.nodeValue:
            uris.append(el)
            
    epsilon = 999999

    for x in range(len(lengths)):
        diff = duration*60000 - int(lengths[x].firstChild.nodeValue)
        if abs(diff) < epsilon:
            epsilon = diff
            link = uris[x].firstChild.nodeValue
        if epsilon < 15000:
            return link
        
    return link
