# Movie

# title,rating,run_time,director,genre

# ARM
# KGF


class Movie:

    title:str

    rating:int

    rin_time:str

    director:str

    genre:str

    def set_movie(self,title,rating,run_time,director,genre):

        self.title=title

        self.rating=rating

        self.run_time=run_time

        self.director=director

        self.genre=genre

    def disply_movie(self):

        print(self.title,self.rating,self.run_time,self.director,self.genre)

movie_instance1=Movie()
movie_instance2=Movie()

movie_instance1.set_movie("ARM",8,"2.30HRS","JITHIN LAL","ADVENTURE")
movie_instance1.disply_movie()

movie_instance2.set_movie("KGF",9.8,"2.30HRS","PRASHAND NEEL","ACTION,CRAME,DRAMA")
movie_instance2.disply_movie()

