imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"),(3, "Mayhem"),(4, "Kentish Town Waltz")
)

for i in imelda:
    if type(i) == tuple:
        for song in i:
            print(song[0], '.\t', song[1])
    else:
        print(i)

# His method

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\t Track number: {}, Title: {}".format(track, title))