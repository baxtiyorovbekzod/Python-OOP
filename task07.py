class Movie:

    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating
    

    def show_summary(self):
        print(f"{self.title}-{self.genre} janridadi film.")
        print(f"Reyting:{self.rating}/10.")       




t1=Movie("Bekorchilar", "comedy", 43 , 9.5)

t1.show_summary()
  
