import sys
import json
import spotipy
import spotipy.util as util

cid = ""
secret = ""
redirect = ""
username = ""
song_count = 5

if len(sys.argv) > 2:
    username = sys.argv[1]
    song_count = int( sys.argv[2] )
    if song_count <= 0:
        print("Song count must be an integer between 1 and 10.")
        sys.exit(0)
    with open("data.json") as f:
        data = json.load(f)
        cid = data["client_id"]
        secret = data["client_secret"]
        redirect = data["redirect_url"]
else:
    print ("Usage: %s username songcount" % (sys.argv[0],))
    sys.exit(0)
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret, redirect_uri=redirect)

if not token:
    sys.exit(0)

sp = spotipy.Spotify(auth=token)
sp.trace = False

artist_dict = {}
keys = []
section = 1
text_doc = open("artists.txt", "r")
for line in text_doc:
    if(line.startswith('#')):
        continue
    if line.startswith('>'):
        section = 1
        keys.append(line[1:-1])
        artist_dict[keys[-1]] = {}
        artist_dict[keys[-1]][str(section)] = []
    else:
        if line.startswith('$'):
            section += 1
            artist_dict[keys[-1]][str(section)] = []
        else:
            artist_dict[keys[-1]][str(section)].append(line[0:-1])

for key in artist_dict:
    print("")
    print(key)
    sp.user_playlist_create(sp.me()['id'], key, True)
    current_playlist_id = sp.current_user_playlists()['items'][0]['id']
    print(current_playlist_id)
    for day in artist_dict[key]:
        print(day)
        print(artist_dict[key][day])
        for artist_name in artist_dict[key][day]:
            print(artist_name)
            results = sp.search('artist:' + artist_name, type='artist', limit=1)
            if len(results['artists']['items']) == 0:
                continue
            artist_id = results['artists']['items'][0]['id']
            i = 0
            tracks = []
            if(len(sp.artist_top_tracks(artist_id)['tracks']) == 0):
                continue
            for track in sp.artist_top_tracks(artist_id)['tracks']:
                if(i < song_count):
                    print(track['name'], track['id'])
                    tracks.append(track['id'])
                    i += 1
            sp.user_playlist_add_tracks(sp.me()['id'], current_playlist_id, tracks)