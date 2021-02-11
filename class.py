class csv:
    mode = ""
    count = ""
    acousticness = ""
    artists = ""
    danceability = ""
    duration_ms = ""
    energy = ""
    instrumentalness = ""
    liveness = ""
    loudness = ""
    speechiness = ""
    tempo = ""
    valence = ""
    popularity = ""
    key = ""

    def __init__(self, mode,count,acousticness,artists,danceability,duration_ms,energy,instrumentalness,liveness,loudness,speechiness,tempo,valence,popularity,key):
        self.mode = mode
        self.count = count
        self.acousticness = acousticness
        self.artists = artists
        self.danceability = danceability
        self.duration_ms = duration_ms
        self.energy = energy
        self.instrumentalness = instrumentalness
        self.loudness = loudness
        self.liveness = liveness
        self.speechiness = speechiness
        self.tempo = tempo
        self.valence = valence
        self.popularity = popularity
        self.key = key

