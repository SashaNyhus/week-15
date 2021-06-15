import requests
import json

def findTitle(query):
    url = "https://imdb8.p.rapidapi.com/title/find"
    queryString = {"q": query}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    res = requests.request("GET", url, headers=headers, params=queryString)
    return json.loads(res.text)

def getKnownFor(actor, actorKey):
    if(actorKey == None):
        actorKey = getActorKey(actor)
        if(actorKey == None):
            return None
    url = "https://imdb8.p.rapidapi.com/actors/get-known-for"
    queryString = {"nconst": actorKey}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers, params=queryString)
    return {"knownFor": json.loads(res.text), "actorKey": actorKey}


def getActorKey(name):
    key = None
    resultsObj = autoComplete(name)
    for result in resultsObj["d"]:
        if(result["id"][0] == "n"):
            key = result["id"]
            break
    return key


def autoComplete(query):
    url = "https://imdb8.p.rapidapi.com/auto-complete"
    queryString = {"q": query}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers, params=queryString)
    return json.loads(res.text)

def getAllFilmography(key):
    url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography"
    queryString = {"nconst": key}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers, params=queryString)
    return json.loads(res.text)


def getFullCredits(titleKey):
    url = "https://imdb8.p.rapidapi.com/title/get-full-credits"
    queryString = {"tconst": titleKey}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers, params=queryString)
    return json.loads(res.text)