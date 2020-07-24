import psycopg2
from datetime import datetime as dt


class VovaPunishDAO:

    def __init__(self, dbname, user, password, host) -> None:
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

    def get_punish(self):
        cursor = self.conn.cursor()
        cursor.execute('select * from public.punish')
        data = cursor.fetchall()
        cursor.close()
        return data

    def insert_punish(self, punish: str):
        cursor = self.conn.cursor()
        cursor.execute('insert into public.stats_punish(punish, date_punish) values(%s, %s)', (punish,  dt.now()))
        self.conn.commit()
        cursor.close()

    def get_stat_punish(self):
        cursor = self.conn.cursor()
        cursor.execute('select punish, count(*) from public.stats_punish group by punish order by 2 desc')
        data = cursor.fetchall()
        cursor.close()
        return data

    def get_all_count_punish(self):
        cursor = self.conn.cursor()
        cursor.execute('select round(exp(sum(ln(cnt)))) from(select type, count(*) cnt from public.punish group by type) as foo')
        data = cursor.fetchall()
        cursor.close()
        return data

    def get_count_punish(self):
        cursor = self.conn.cursor()
        cursor.execute('select count(distinct punish) from public.stats_punish')
        data = cursor.fetchall()
        cursor.close()
        return data





