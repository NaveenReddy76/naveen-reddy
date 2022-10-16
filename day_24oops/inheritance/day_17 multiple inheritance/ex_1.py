class a:
    def tollywood(self):
        self.actors='power star'
        self.no_movies='30'
        self.awards='189'
        print(self.awards,self.actors,self.no_movies)

class b:
    def bollywood(self):
        self.actor='sushanth'
        self.no_movieslist='15'
        self.awards_won='40'
        print(self.actor,self.no_movieslist,self.awards_won)

class c :
    def kadapa_halls(self):
        self.prasad_hall='rayachoty'
        self.no_seats='200'
        self.prsnt_movie='vikram'

class d (a,b ,c):
    def show_details(self):
        self.mrng='10 am'
        self.aftrnoon='2 pm'
        print(self.mrng,self.aftrnoon)

D=d()
D.show_details()
D.kadapa_halls()
D.bollywood()
D.tollywood()