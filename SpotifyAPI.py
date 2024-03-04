# Setting Libraries
from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get


# Load environment file containing the keys
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


# Using CI and CS created an authorization string and encoded with base64
def get_token():
    auth_string = client_id + ":" + client_secret  # keys need to be concantenated
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    # Sending request to the following URL
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # Request body (grant-type)
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

    # Authorization request for header
def get_auth_header(token):
    return{"Authorization": "Bearer " + token}
    
    # Using the Endpoint url for searching 
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("No artist with this name exists... ")
        return None
    return json_result[0]

    # Using the Endpoint url for getting songs from artist
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

token = get_token()
result = search_for_artist(token, "Rauw Alejandro")
artist_id = result["id"]
songs = get_songs_by_artist(token, artist_id)

# Looping to get the top 10 songs in the USA
for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}")

with open("rasongs.json", "w", encoding="utf-8") as f:
    json.dump(songs, f, ensure_ascii=False, indent=4)