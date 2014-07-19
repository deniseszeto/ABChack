from urllib.request import urlopen
from xml.dom import minidom

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
