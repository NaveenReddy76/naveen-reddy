from abc import ABC  , abstractmethod
class movies(ABC):
    @abstractmethod
    def telugu_actors(self):
        pass


class hits(movies):
    def telugu_actors(self):
        self.power_hits = 30
        self.mega_hits = 100
        print(self.power_hits, self.mega_hits)


obj = hits()
obj.telugu_actors()
obj.telugu_actors()


