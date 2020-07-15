
import random

class VovaPunishService:

    def __init__(self, dbApi) -> None:
        self.dbApi = dbApi
        self.template = '1 2 3 4'

    def makePunish(self):
        strok = self.template
        data = self.dbApi.getPunish()
        slova = {}
        for i in data:
            if slova.get(int(i[2])) is None:
                slova[int(i[2])] = [i[1]]
            else:
                slova.get(int(i[2])).append(i[1])
        for i in slova:
            strok = strok.replace(str(i), self.getWord(slova.get(i)))
        return strok

    def getWord(self, mass) -> str:
        lm = len(mass)
        ran = random.randint(0, lm - 1)
        word = mass[ran]
        return word









