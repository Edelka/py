import sqlite3
from datetime import datetime


class DBConnection:
    def __init__(self, database_name='news.db'):
        with sqlite3.connect(database_name) as self.connection:
            self.cur = self.connection.cursor()
            print('Connected')

    def create_table_news(self):
        self.cur.execute(
            'create table if not exists News (text char, city char, date char)')

    def create_table_cities(self):
        self.cur.execute(
            'create table if not exists City (city char, lon real, lat real)')

    def select_city(self, city1):
        return self.cur.execute(f"SELECT city, lon, lat FROM City WHERE city = \'{city1}\'").fetchall()


    def insert_city(self, inp1, inp2, inp3):
        self.cur.execute(f"insert into City (city, lon, lat) values ('{inp1}\', \'{inp2}\', \'{inp3}\')")
        print(f"Inserted into City")
        self.connection.commit()

    # move to each class
    # def insert_news(self, news_to_insert): # text, city, date_time=datetime.now().strftime("%d/%m/%Y, %H:%M")):
    #     # self.cur.execute(f"insert into News values ('{text}\', \'{city}\', \'{date_time}\')")
    #     self.cur.execute(f"insert into News values ('{news_to_insert.text}\', \'{news_to_insert.city}\', \'{news_to_insert.date_time}\')")
    #     print(f"Inserted into News")
    #     self.connection.commit()

    def select(self, table, columns):
        return self.cur.execute(f"select {columns} from {table}").fetchall()[-1]  # select last tuple

    def close_cursor(self):
        self.cur.close()
        self.connection.close()
