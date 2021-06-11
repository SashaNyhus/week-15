import requests
import json


def get_user_song():
    search_query = input("search for a song")
    search_results = search_for_song(search_query)
    result_array_to_print = get_result_array_to_print(search_results)
    print(*result_array_to_print, sep=", ")


def search_for_song(song):
    url = "https://shazam.p.rapidapi.com/search"
    query_str = {"term": song, "locale": "en-US", "offset": "0", "limit": "5"}
    headers = {
        'x-rapidapi-key': "fa28eee3eemsh74c42be02bf9b23p141db5jsnbfb2a373758a",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
    res = requests.request("GET", url, headers=headers, params=query_str)
    return json.loads(res.text)


def get_result_array_to_print(results_obj):
    results_array = results_obj["tracks"]["hits"]
    return map(
        lambda obj: obj["track"]["title"] + " by " + obj["track"]["subtitle"],
        results_array
        )


get_user_song()
