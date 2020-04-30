import spotipy
import spotipy.util as util
import json

token = ""
username = "finnyboy1234567"
scope = "user-read-currently-playing app-remote-control streaming user-read-playback-state user-modify-playback-state user-read-currently-playing"

def start():
    apiKey = json.load(open("apiKey.json"))
    token = util.prompt_for_user_token(username, scope, apiKey['id'], apiKey['secret'], 'https://raw.githubusercontent.com/innif/Listify/master/response.txt')

start()

