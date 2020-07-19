import random


class VovaPunishService:

    def __init__(self, dbApi) -> None:
        self.word_to_replace = {"  ": " ",
                                " ,": ","}
        self.dbApi = dbApi
        self.template = '1 2 3 4'
        self.statsPunishInfo = {}

    def make_punish(self):
        strok = self.template
        data = self.dbApi.get_punish()
        slova = {}
        for i in data:
            if slova.get(int(i[2])) is None:
                slova[int(i[2])] = [i[1]]
            else:
                slova.get(int(i[2])).append(i[1])
        for i in slova:
            strok = strok.replace(str(i), self.get_word(slova.get(i)))
        strok = self.replace_all(strok)
        self.add_stat_punish(strok)
        return strok

    def get_word(self, mass) -> str:
        lm = len(mass)
        ran = random.randint(0, lm - 1)
        word = mass[ran]
        return word

    def add_stat_punish(self, punish: str):
        self.dbApi.insert_punish(punish)

    def get_stat_punish(self) -> str:
        str_format = "{0}:{1}"
        stat_pun = self.dbApi.get_stat_punish()
        if len(stat_pun) != 0:
            return "\n".join([str_format.format(i[0], i[1]) for i in stat_pun])
        else:
            return "Ничего нет("

    def replace_all(self, punish: str) -> str:
        for k, v in self.word_to_replace.items():
            punish = punish.replace(k, v)
        return punish
