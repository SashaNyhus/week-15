import requests
import json

def search(song, page):
    url = "https://shazam.p.rapidapi.com/search"
    query_str = {"term": song, "locale": "en-US", "offset": page, "limit": "5"}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
    res = requests.request("GET", url, headers=headers, params=query_str)
    return json.loads(res.text)

def get_recommendations(song_key):
    url = "https://shazam.p.rapidapi.com/songs/list-recommendations"
    query_str = {"key": song_key, "locale": "en-US"}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
    res = requests.request("GET", url, headers=headers, params=query_str)
    return json.loads(res.text)
