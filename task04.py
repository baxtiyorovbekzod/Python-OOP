class Movie:

    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

t1=Movie("Bekorchilar", "comedy", 43 , 9.5)


print(t1.title)
print(t1.genre)
print(t1.duration)
print(t1.rating)   