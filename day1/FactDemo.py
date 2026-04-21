class Team:
    def __init__(self): self.__rankings = ["india","australia","new zealand"]
    def viewStats(self,position=0):
        if position!=0: return self.__rankings[position-1]
        else: return self.__rankings
class Bowlers:
    def __init__(self): self.__bowlers = ["Jadeja","Ashwin","Bumra"]
    def viewStats(self,position=0):
        if position!=0: return self.__bowlers[position-1]
        else: return self.__bowlers
class ICC:
    @staticmethod
    def see(which):
        if which == "team": return Team()
        else: return Bowlers()
# main execution
stat = ICC.see("team")
print(stat.viewStats())
stat = ICC.see("bowlers")
print(stat.viewStats(1))