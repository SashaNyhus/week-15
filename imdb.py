import requests
import json


def findTitle(query):
    print("fetching title")
    url = "https://imdb8.p.rapidapi.com/title/find"
    queryString = {"q": query}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    res = requests.request("GET", url, headers=headers, params=queryString)
    return json.loads(res.text)


def getKnownFor(actor, actorKey):
    if(actorKey is None):
        actorData = getActorData(actor)
        if(actorData is None):
            return None
        actor = actorData["name"]
        actorKey = actorData["key"]
    print("fetching Known For list")
    url = "https://imdb8.p.rapidapi.com/actors/get-known-for"
    queryString = {"nconst": actorKey}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers, params=queryString)
    dataToReturn = {"knownFor": json.loads(res.text), "actorKey": actorKey, "name": actor}
    return dataToReturn


def getActorData(nameInput):
    fetchedKey = None
    fetchedName = None
    resultsObj = autoComplete(nameInput)
    for result in resultsObj["d"]:
        if(result["id"][0] == "n"):
            fetchedKey = result["id"]
            fetchedName = result["l"]
            break
    data = {"name": fetchedName, "key": fetchedKey}
    return data


def autoComplete(query):
    print("using autocomplete endpoint")
    url = "https://imdb8.p.rapidapi.com/auto-complete"
    queryString = {"q": query}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers, params=queryString)
    return json.loads(res.text)


def getAllFilmography(key):
    print("fetching full filmography")
    url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography"
    queryString = {"nconst": key}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers, params=queryString)
    return json.loads(res.text)


def getFullCredits(titleKey):
    print("fetching full credits")
    url = "https://imdb8.p.rapidapi.com/title/get-full-credits"
    queryString = {"tconst": titleKey}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers, params=queryString)
    return json.loads(res.text)
