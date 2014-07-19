import soundcloud

# create a client object with your app credentials
client = soundcloud.Client(client_id='93fbdae95f70cd94b70864746295c28f')

# fetch track to stream
track = client.get('/tracks/293')

# get the tracks streaming URL
stream_url = client.get(track.stream_url, allow_redirects=False)

# print the tracks stream URL
print stream_url.location


tracks = client.get('/tracks', limit=10)
for track in tracks:
    print track.title
app = client.get('/apps/124')
print app.permalink_url

print("hi world") #kai
print("bye world") #jackson