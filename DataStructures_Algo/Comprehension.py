class ComprehensionEg:

    def __init__(self):
        self.list_compre()
        self.dict_compre()
        self.set_compre()

    def list_compre(self):

        even = [2, 4, 6, 8]
        odd = [1, 3, 5, 7]

        # evensqr = list(map(lambda x : x**2, filter(lambda x: x>= 4 and x<40, even)))
        # oddsqr = list(map(lambda x : x**2, filter(lambda x: x>= 4 and x<40, odd)))

        evensqr = [e**2 for e in even]
        oddsqr = [o**2 for o in odd if o > 3 and o < 40]
        print(evensqr, end='\n')
        print(oddsqr)

    def dict_compre(self):

        temps = [0, 2, 4, 30]

        tempDict = {t: (t*9/5)+32 for t in temps if t < 100}

        team1 = {"apple": 1, "chickoo": 2}
        team2 = {"grapes": 3, "berry": 4}
        mergedteam = {x: y for team in (team1, team2) for x, y in team.items()}

        print(tempDict)
        print(mergedteam)

    def set_compre(self):

        l = [2, 2, 4, 5, 6]
        lc = [i**2 for i in l]
        sc = {i**2 for i in l}
        print(lc)
        print(sc)


if __name__ == "__main__":
    obj = ComprehensionEg()
