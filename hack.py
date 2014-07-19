from urllib.request import urlopen
from xml.dom import minidom

# Assume *optional = (genre, author, etc..)
def findSong(duration, author="", genre="electronic"):
    CLIENT_ID = '93fbdae95f70cd94b70864746295c28f'
    
    url = "http://api.soundcloud.com/tracks?client_id=" + CLIENT_ID

    try:
        duration = float(duration) # Converts Duration from String
    except:
        duration = 5.0 # Default Error Handling Duration

    url += "&filter.duration="
    if duration < 2:
        url += "short"
    elif duration < 10:
        url += "medium"
    elif duration < 30:
        url += "long"
    else:
        url += "epic"
        
    url += "&genre=" + genre + "&q=" + author

    page = urlopen(url)
    xmldoc = minidom.parse(page)
    lengths = xmldoc.getElementsByTagName('duration')
    uris = []
    for el in xmldoc.getElementsByTagName('uri'):
        if "tracks" in el.firstChild.nodeValue:
            uris.append(el)
            
    epsilon = float('inf')

    for x in range(len(lengths)):
        diff = abs(duration * 60000 - float(lengths[x].firstChild.nodeValue))
        if diff < epsilon:
            epsilon = diff
            link = uris[x].firstChild.nodeValue
        if epsilon < 10000: # Tolerance of 10 Seconds
            return link[33:]
        
    return link[33:]
