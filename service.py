import random
from datetime import datetime as dt
from Dictionaries import SettingsDict as SetDict
from DBApi import VovaPunishDAO
from Utils import Support


class VovaPunishService:

    def __init__(self, db_api: VovaPunishDAO) -> None:
        self.dbApi = db_api
        self.template = '1 2 3 4'
        self.settings_to_view = [SetDict.chance()]
        self.util = Support()

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
        strok = self.util.replace_all(strok)
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
        stat_pun = self.dbApi.get_stat_punish()
        if len(stat_pun) != 0:
            return self.util.make_message_from_list("ТОП 10 ОСКОРБЛЕНИЙ:",
                                                    stat_pun[0: 10],
                                                    self.get_count_of_all_punish())
        else:
            return "Ничего нет("

    def get_count_of_all_punish(self) -> str:
        all_cnt = self.dbApi.get_all_count_punish()
        cur_cnt = self.dbApi.get_count_punish()
        all_cnt = 0 if len(all_cnt) == 0 else int(all_cnt[0][0])
        cur_cnt = 0 if len(cur_cnt) == 0 else int(cur_cnt[0][0])
        if all_cnt != 0:
            data = 'Открыто оскорблений {0} из {1} - {2}%'.format(cur_cnt, all_cnt, round(cur_cnt/all_cnt*100, 2))
        else:
            data = 'Нет слов'
        return data

    def need_send(self, ms_date: int) -> bool:
        rand_num = random.randint(1, 100)
        punish_chance = int(self.dbApi.get_settings(SetDict.chance()))
        diff_data = dt.now() - dt.fromtimestamp(ms_date)
        if rand_num <= punish_chance and abs(diff_data.total_seconds()) < 10:
            return True
        return False

    def get_all_settings(self) -> str:
        settings = {}
        for setting in self.settings_to_view:
            settings[setting] = self.dbApi.get_settings(setting)
        return self.util.make_message_from_dict("Настройки:", settings)
