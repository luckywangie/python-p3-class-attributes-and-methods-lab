class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the song count
        Song.add_song_to_count()
        
        # Add genre and artist to respective class attributes
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        
        # Update genre count and artist count
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the song count whenever a new song is created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds the genre to the genres list if it's not already there."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds the artist to the artists list if it's not already there."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Adds to the genre count dictionary, tracking the number of songs per genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Adds to the artist count dictionary, tracking the number of songs per artist."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Test the Song class
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Hotline Bling", "Drake", "Pop")
song3 = Song("Halo", "Beyonce", "Pop")
song4 = Song("Empire State of Mind", "Jay-Z", "Rap")
song5 = Song("Crazy In Love", "Beyonce", "Pop")
song6 = Song("God's Plan", "Drake", "Rap")

# Verify the outputs
print("Total number of songs:", Song.count)  
print("Genres:", Song.genres)  
print("Artists:", Song.artists)  
print("Genre count:", Song.genre_count)  
print("Artist count:", Song.artist_count)  
