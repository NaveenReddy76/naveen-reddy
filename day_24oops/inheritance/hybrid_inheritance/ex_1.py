class prabhas:
    def all_films(self):
        self.firstfilm='darling'
        self.secondmovie='mirchi'
        self.thirdfilm='bb1'
        print(self.firstfilm,self.secondmovie,self.thirdfilm)


class anushka(prabhas):
    def movies(self):
        self.entry='vikram'
        self.latest='bb2'
        print(self.latest,self.entry)

class ram(anushka):
    def no_hits(self):
        self.awards='90'
        self.hits='10'
        self.upcoming='5'
        print(self.awards,self.hits,self.upcoming)

R=ram()
R.movies()
R.no_hits()
R.all_films()

print("___"*20)
A=anushka()
A.movies()
A.all_films()