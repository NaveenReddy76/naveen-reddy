class kings:
    def no_hero2(self):
        self.name_1='all heros'
        self.countrys='india'
        self.state='andhra pradesh'
        print(self.countrys,self.name_1,self.state)

class queens(kings) :
    def telugu_hero(self):
        self.firsthero='power star'
        self.secondhero='mega star'
        self.thirdstar='mega power star'
        print(self.firsthero,self.secondhero,self.thirdstar)

Q=queens()
Q.telugu_hero()
Q.no_hero2()

class manthri(kings):
    def areas(self):
        self.local='kadapa'
        self.kingdom='sangavi'
        self.manthriname='raji'
        print(self.local,self.manthriname,self.kingdom)

M=manthri()
M.areas()
M.no_hero2()


class sangavi(kings):
    def stores(self):
        self.kingname='naveen'
        self.queenname='sangavi'
        self.manthariname='raji'


S=sangavi()
S.stores()
S.no_hero2()

