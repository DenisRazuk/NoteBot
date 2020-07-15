import psycopg2


class VovaPunishDAO:

    def __init__(self, dbname, user, password, host) -> None:
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)


    def getPunish(self):
        cursor = self.conn.cursor()
        cursor.execute('select * from public.punish')
        data = cursor.fetchall()
        cursor.close()
        return data



