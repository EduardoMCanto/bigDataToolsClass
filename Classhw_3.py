from db_config import get_redis_connection

r = get_redis_connection()

file_path = "./RAsongs.json"

# Setting classes for different attributes (songs)
class song:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def artist(self):
        print(f"{self.name} this song was released in the following year {self.date}")
        

my_song = song("Diluvio", 2023)
other_song = song("LOKERA", 2022)

my_song.artist()
other_song.artist()

# Setting classes for different attributes (popularity)
class artist:
    def __init__(self, song, date):
        self.song = song
        self.date = date

    def singer(self):
        print(f"{self.song} was a total hit within this year {self.date}")
        

my_singer = artist("Saturno", 2021)
other_singer = artist("Marico Barjas", 2021)

my_singer.singer()
other_singer.singer()

# Setting classes for different attributes (popularity)
class hit:
    def __init__(self, track, popularity):
        self.track = track
        self.popularity = popularity

    def newone(self):
        print(f"{self.track} this track has a total popularity of {self.date}")
        

my_hits = hit("RR", 95)
other_hits = hit("Desesperados", 90)

my_hits.newone()
other_hits.newone()
