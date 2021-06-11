import requests
import json


def get_user_song_key():
    search_query = input("Search for a song")
    search_results = search_for_song(search_query)
    results_to_print = get_track_results_to_print(search_results)
    print("We found:")
    print(*results_to_print, sep="\n")
    song_index = int(input(
        "Which song did you mean? Type the number next to it"
        ))
    return search_results["tracks"]["hits"][song_index]["track"]["key"]


def search_for_song(song):
    url = "https://shazam.p.rapidapi.com/search"
    query_str = {"term": song, "locale": "en-US", "offset": "0", "limit": "5"}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
    res = requests.request("GET", url, headers=headers, params=query_str)
    return json.loads(res.text)


def get_track_results_to_print(results_obj):
    track_results = results_obj["tracks"]["hits"]
    array_to_print = []
    track_index = 0
    for obj in track_results:
        array_to_print.append(
            str(track_index) + ") " +
            obj["track"]["title"] +
            " by " + obj["track"]["subtitle"])
        track_index += 1
    return array_to_print


def get_user_song_suggestions():
    user_song_key = get_user_song_key()
    print(user_song_key)
    suggestions_obj = fetch_suggestions(user_song_key)
    if(suggestions_obj):
        suggestions_array = suggestions_obj["tracks"]
        printable_array = []
        for obj in suggestions_array:
            printable_array.append(
                obj["title"] +
                " by " + obj["subtitle"]
            )
        print("based on that song, we suggest:")
        print(*printable_array, sep="\n")
    else:
        print("we couldn't find any other songs like that one")


def fetch_suggestions(song_key):
    url = "https://shazam.p.rapidapi.com/songs/list-recommendations"
    query_str = {"key": song_key, "locale": "en-US"}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
    res = requests.request("GET", url, headers=headers, params=query_str)
    return json.loads(res.text)


get_user_song_suggestions()

# unused loop
# while(track_index < len(track_results)):
#     array_to_print.append(
#         str(track_index) + ") " +
#         track_results[track_index]["track"]["title"] +
#         " by " + track_results[track_index]["track"]["subtitle"]
#     )
#     track_index += 1
