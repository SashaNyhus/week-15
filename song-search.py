import requests
import json


def get_user_song_key(search_term, results_page):
    search_results = search_for_song(search_term, results_page)
    results_to_print = get_track_results_to_print(search_results)
    print("We found:")
    print(*results_to_print, sep="\n")
    song_index = int(input(
        "Which song did you mean?\n"
        "Type the number next to it, or 0 if none of them match"
        ))
    if(song_index == 0):
        return 0
    return search_results["tracks"]["hits"][(song_index - 1)]["track"]["key"]


def search_for_song(song, page):
    url = "https://shazam.p.rapidapi.com/search"
    query_str = {"term": song, "locale": "en-US", "offset": page, "limit": "5"}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
    res = requests.request("GET", url, headers=headers, params=query_str)
    return json.loads(res.text)


def get_track_results_to_print(results_obj):
    track_results = results_obj["tracks"]["hits"]
    array_to_print = []
    track_index = 1
    for obj in track_results:
        array_to_print.append(
            str(track_index) + ") " +
            obj["track"]["title"] +
            " by " + obj["track"]["subtitle"])
        track_index += 1
    return array_to_print


def get_user_song_suggestions():
    choosing_song = True
    search_query = input("Search for a song")
    page_offset = 0
    while(choosing_song):
        user_song_key = get_user_song_key(search_query, page_offset)
        if(user_song_key == 0):
            print(
                "0) new search\n"
                "1) show me the next page of results\n"
                "2) cancel program"
            )
            decision = int(input("what would you like to do?"))
            if(decision == 0):
                search_query = input("Search for a song")
                page_offset = 0
                continue
            elif(decision == 1):
                page_offset += 5
                continue
            else:
                return
        else:
            choosing_song = False
            break
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
