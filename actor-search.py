import imdb

def actorSearch():
    nameKnown = input("Do you know the actor's name? Type y/n")
    if(nameKnown == "y"):
        actorName = input("Type the name")
        actorKey = None
    else:
        actorData = getActorFromCharacter()
        if actorData == None:
            return
        actorName = actorData["name"]
        actorKey = actorData["actorKey"]
    actorKnownForData = imdb.getKnownFor(actorName, actorKey)
    knownFor = actorKnownForData["knownFor"]
    actorKey = actorKnownForData["actorKey"]
    if(knownFor == None):
        print("no results found")
        return
    printableKnownFor = []
    for result in knownFor:
        summary = result["summary"]
        role = ""
        if "characters" in summary:
            role = (summary["category"] + "- " + ", ".join(summary["characters"]))
        elif "category" in summary:
            role = summary["category"]
        printableKnownFor.append(
            result["title"]["title"] + 
            " (" + str(result["title"]["year"]) + " " + result["title"]["titleType"] + "): " +
            role
        )
    print(actorName + " is best known for")
    print(*printableKnownFor, sep="\n")
    getMore = input("See all filmography? y/n")
    if (getMore == "y"):
        filmography = imdb.getAllFilmography(actorKey)
        printableFilmography = []
        for title in filmography["filmography"]:
            titleStatus = ""
            role = ""
            if "year" in title:
                titleStatus = str(title["year"])
            elif "status" in title:
                titleStatus = title["status"]
            if "characters" in title:
                role = (title["category"] + "- " + ", ".join(title["characters"]))
            elif "category" in title:
                role = title["category"]
            printableFilmography.append(
                title["title"] + " (" + title["titleType"] + ", " + titleStatus + "): " + role
            )
        keepViewing = True
        indexStart = 0
        page = 1
        while(keepViewing):
            print(actorName + " filmography, page " + str(page))
            print("\n".join(printableFilmography[indexStart:(indexStart + 14)]))
            doNext = input(
                "0) end program \n"
                "1) see next 15 results \n"
                "2) see previous 15 results"
            )
            if doNext == "1":
                indexStart += 15
                page += 1
                if indexStart > (len(printableFilmography)):
                    print("end of list reached. returned to top")
                    indexStart = 0
                    page = 1
                continue
            elif doNext == "2":
                if indexStart > 0:
                    indexStart -=15
                    page -= 1
                else:
                    print("already at beginning of list")
                continue
            else: break
    return

def getActorFromCharacter():
    movie = input("What's the movie (or other media)?")
    character = input("What's the character's name?")
    name = ""
    key = ""
    foundIt = ""
    print("searching database - this may take a moment")
    movieResults = imdb.autoComplete(movie)
    for movieResult in movieResults["d"]:
        castList = imdb.getFullCredits(movieResult["id"])["cast"]
        for castMember in castList:
            if character in castMember["characters"]:
                year = movieResult["y"]
                if "yr" in movieResult:
                    year = movieResult["yr"]
                foundIt = input("Did you mean " + character + " played by " + castMember["name"] + " in " + movieResult["l"] + " (" + year + " " + movieResult["q"] + ")? y/n")
                if foundIt == "y":
                    name = castMember["name"]
                    key = castMember["id"].removeprefix("/name/")
                    break
        if foundIt == "y":
            break
    if foundIt != "y":
        print("sorry, we couldn't find that")
        return None
    actorData = {"name": name, "actorKey": key}
    return actorData

actorSearch()