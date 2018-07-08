# top5playlist.py

## A lightweight script making use of the spotipy library to bulk-add a collection of artists' top songs to a playlist on spotify.

* Artists are listed in a plain text file *artists.txt* .
* \> indents are used to indicate a new playlist title. All artist names under a title are added into that playlist.
You can specify a new playlist title at any time.
* \# Hashtags are commented out, they aren't read by the script.
* $ dollar signs are used to break the list apart. In the Reading Festival example they are used to seperate the different artists by the days that they perform.

You will need access to a spotify app which can easily be created at https://developer.spotify.com/dashboard/ Once you create your app, add the client id and client secret into the data.json file. You will also need to set a callback redirect url, for now something we only need a simple temporary location, http://localhost:8888/callback/ will do just fine. Add this redirect url to the data.json file too.

To run the script cd into the folder containing the script and run
```python
python top5playlist.py <username> <song_count>
```
where *username* is your spotify username and *song_count* is the number of top songs you want to add from each artist, up to 10.
After you run the script you will be promted with a web page from spotify asking for confirmation that you want to use the app. Click yes and a new playlist will be created and will start filling up with songs.
