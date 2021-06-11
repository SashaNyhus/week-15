import shazam


suggest_a_song()


def suggest_a_song():
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
    print("song key is " + user_song_key)
    suggestions_obj = shazam.get_recommendations(user_song_key)
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


def get_user_song_key(search_term, results_page):
    search_results = shazam.search(search_term, results_page)
    results_to_print = make_search_results_printable(search_results)
    print("We found:")
    print(*results_to_print, sep="\n")
    song_index = int(input(
        "Which song did you mean?\n"
        "Type the number next to it, or 0 if none of them match"
        ))
    if(song_index == 0):
        return 0
    return search_results["tracks"]["hits"][(song_index - 1)]["track"]["key"]


def make_search_results_printable(results_obj):
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









# unused loop
# while(track_index < len(track_results)):
#     array_to_print.append(
#         str(track_index) + ") " +
#         track_results[track_index]["track"]["title"] +
#         " by " + track_results[track_index]["track"]["subtitle"]
#     )
#     track_index += 1
