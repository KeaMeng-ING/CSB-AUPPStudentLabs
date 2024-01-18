import os
import pandas as pd
import random
os.system("cls")
class Song:
    def __init__(self, title, artist, album, genre, length):
        self.details = (title, artist, album, genre, length)

class MusicLibrary:
    def __init__(self):
        self.songs = set()

    def add_song(self, song):
        self.songs.add(song.details)

    def get_songs_by_attribute(self, attribute, value):
        """ attribute 0 for song title, 1 for artist, 2 for album, 3 for genre, 4 for length """
        print(f"\n=============== Search for {value} ================")

        if attribute == 'title':
            attribute = 0
        elif attribute == 'artist':
            attribute = 1
        elif attribute == 'album':
            attribute = 2
        elif attribute == 'genre':  
            attribute = 3
        elif attribute == 'length':
            attribute = 4
    
        return [song for song in self.songs if song[attribute] == value][0]

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song.details)

    def remove_song(self, song):
        self.songs.remove(song.details)

    def reorder_songs(self):
        random.shuffle(self.songs)

    def display_playlist(self):
        data = {'Title': [], 'Artist': [], 'Album': [], 'Genre': [], 'Length': []}
        for song in self.songs:
            data['Title'].append(song[0])
            data['Artist'].append(song[1])
            data['Album'].append(song[2])
            data['Genre'].append(song[3])
            data['Length'].append(song[4])
        df = pd.DataFrame(data)
        df.index = df.index + 1
        print("\n===========================Playlist===========================")
        print(df)


def main():
    # Create a MusicLibrary
    library = MusicLibrary()

    # Add some songs to the library
    song1 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", "Rock", "6:07")
    song2 = Song("Hotel California", "Eagles", "Hotel California", "Rock", "6:30")
    song3 = Song("Imagine", "John Lennon", "Imagine", "Pop", "3:01")
    library.add_song(song1)
    library.add_song(song2)
    library.add_song(song3)

    # Get songs by attribute  -- Sample
    # print(library.get_songs_by_attribute('artist', "Queen"))
    
    # print(library.get_songs_by_attribute('album', "Imagine"))
    # print(library.get_songs_by_attribute('genre', "Rock"))
    # print(library.get_songs_by_attribute('length', "6:30"))


    playlist = Playlist("My Playlist")
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)
    # playlist.display_playlist()
    # playlist.remove_song(song1)
    # playlist.reorder_songs()
    playlist.display_playlist()

    print(library.get_songs_by_attribute('title', "Hotel California"))
    

main()