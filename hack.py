# TODO: Add "Randomizer", Update Webpage to show more than 50 items
#       Optimize Parser

from urllib.request import urlopen
from xml.dom import minidom

# Assume *optional = (genre, title, etc..)
def findSong(duration, title="", genre="electronic"):
    CLIENT_ID = '93fbdae95f70cd94b70864746295c28f'
    
    url = "http://api.soundcloud.com/tracks?client_id=" + CLIENT_ID

    try:
        duration = float(duration) # Converts Duration from String
    except:
        duration = 5.0 # Default Error Handling Duration
    title = title.replace(" ", "_")
    genre = genre.replace(" ", "_")

    url += "&filter.duration="
    if duration < 2:
        url += "short"
    elif duration < 10:
        url += "medium"
    elif duration < 30:
        url += "long"
    else:
        url += "epic"
        
    url += "&genre=" + genre + "&q=" + title

    page = urlopen(url)
    xmldoc = minidom.parse(page)
    lengths = xmldoc.getElementsByTagName('duration')
    uris = []
    for el in xmldoc.getElementsByTagName('uri'):
        if "tracks" in el.firstChild.nodeValue:
            uris.append(el)
            
    epsilon = float('inf')
    link = "http://api.soundcloud.com/tracks/159352695"
    
    for x in range(len(lengths)):
        diff = abs(duration * 60000 - float(lengths[x].firstChild.nodeValue))
        if diff < epsilon:
            epsilon = diff
            link = uris[x].firstChild.nodeValue
        if epsilon < 10000: # Tolerance of 10 Seconds
            return link[33:]
        
    return link[33:]
