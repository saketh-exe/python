from dotenv import load_dotenv
import base64
import os
from requests import post,get
import json
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_sec = os.getenv("CLIENT_SEC")

def get_tok():
    # authorization code , Authorization: Basic <base64 encoded client_id:client_secret>
    auth_str = client_id+":"+client_sec
    auth_bytes = auth_str.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"


    headers = {"Authorization": "Basic "+ auth_base64,
               "Content-Type": "application/x-www-form-urlencoded"}
    
    data = {"grant_type": "client_credentials"}

    result = post(url,headers=headers,data=data)
    json_result = json.loads(result.content)
    try:
        token = json_result['access_token']
        return token
    except:
        print(json_result)
        exit()
def get_header(token):
    return{"Authorization":"Bearer "+token}
def search_for_artist(token,artist_name):
    url = "https://api.spotify.com/v1/search"
    headers =get_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query
    result = get(query_url,headers=headers)
    json_result = json.loads(result.content)
    return json_result    
def artist_id(txt):
    details = txt["artists"]
    details0 = details["items"]
    details1 = details0[0]
    id = details1["id"]
    return id
def songs_by_artist(token,artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers =get_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result
def get_user_id(token):
    url = "https://api.spotify.com/v1/me"
    headers =get_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result
def player(token):
    url = f"https://api.spotify.com/v1/me/player/currently-playing"
    headers =get_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result


token = get_tok()
#txt = search_for_artist(token,"")
#id = artist_id(txt)
#songs = songs_by_artist(token,id)

#for idx, song in enumerate(songs):
 #   print(f"{idx +1}, {song['name']}")

c = player(token)
print(c)