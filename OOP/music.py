class Song:

    def __init__(self, name, duration=0):
        self.name = name
        self.duration = duration

    def __str__(self):
        return self.name


class Album:

    def __init__(self, name, artist_name):
        self.name = name
        self.artist_name = artist_name
        self.songs_list = []

    def addSongToAlbum(self, title):
        newSong = Song(title)
        self.songs_list.append(newSong)

    def __str__(self):
        print(f"\nContent of: {self.name}")
        for element in self.songs_list:
            print(element)
        return ''


class Artist:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def addAlbum(self, albumName):
        newAlbum = Album(albumName.name,self.albums)
        self.albums.append(newAlbum)

    def addSong(self,name, year, title):
        album_found = findObject(name, self.albums)
        if album_found is None:
            print("Not found!")
            album_found = Album(name, self.name)
            self.albums.append(album_found)
        else:
            print("Found" + name)
        album_found.addSongToAlbum(title)


def findObject(searchedItem, listOfItems):
    for item in listOfItems:
        if item.name == searchedItem:
            return item
    else:
        return None


with open("checkfile.txt", 'r') as albums:
    artists_list = []
    song_list =[]

    for line in albums:
        listOfStrings = line.strip('\n').split('\t')

        artist_name = listOfStrings[0]
        album_name = listOfStrings[1]
        year = listOfStrings[2]
        song_name = listOfStrings[3]

        newArtist = findObject(artist_name, artists_list)

        if newArtist is None:
            newArtist = Artist(artist_name)
            newArtist.addSong(album_name, year, song_name)
            artists_list.append(newArtist)
            song_list.append(Song(song_name))
        else:
            newArtist.addSong(album_name, year, song_name)
            song_list.append(Song(song_name))


for artist in artists_list:
    print("****************" + artist.name + "****************")
    for album in artist.albums:
        print(album.name)
        for song in album.songs_list:
            print("\t\t" + song.name)

print("Number of artists:" + str(len(artists_list)))
print("Number of songs:" + str(len(song_list)))