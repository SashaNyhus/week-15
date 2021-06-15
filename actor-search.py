import imdb

def actorSearch():
    nameKnown = input("Do you know the actor's name? Type y/n")
    if(nameKnown == "y"):
        actorName = input("Type the name")
    else:
        actorName = getActorFromCharacter()
    actorKnownForData = imdb.getKnownFor(actorName, None)
    knownFor = actorKnownForData["knownFor"]
    actorKey = actorKnownForData["actorKey"]
    if(knownFor == None):
        print("no results found")
        return
    printableKnownFor = []
    for result in knownFor:
        printableKnownFor.append(
            result["title"]["title"] + 
            " (" + str(result["title"]["year"]) + " " + result["title"]["titleType"] + "): " +
            (", ".join(result["summary"]["characters"]) or result["summary"]["category"])
        )
    print(actorName + " is best known for")
    print(*printableKnownFor, sep="\n")
    # getMore = input("See all filmography? y/n")
    # if (getMore == "y"):
    #     filmography = imdb.getAllFilmography(actorKey)
    #     printableFilmography = []
    #     for title in filmography["filmography"]:
    #         printableFilmography.append(
    #             title["title"] + " (" + title["titleType"] + ", " + (str(title["year"]) or title["status"]) + "): " +
    #             # (", ".join(title["characters"]) or 
    #             result["category"]
    #         )
    return

def getActorFromCharacter():
    movie = input("What's the movie (or other media)?")
    character = input("What's the character's name?")
    return

actorSearch()