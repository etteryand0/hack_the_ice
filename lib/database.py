import sqlite3


class Database:
    def __init__(self):
        # Обозначаем нужные константы - колонки
        # part1 A-P
        # B - 1
        # D - 3
        self.part1 = {'B': 1, 'D': 3}
        # part3 AG-BR
        # AL - 6  # AM - 7
        # AR - 12
        self.part3 = {'AL': 6, 'AM': 7, 'AR': 12}
        # part5 BU-
        # BV - 2  # BY - 5
        # CE - 11
        self.part4 = {'BV': 2, 'BY': 5, 'CE': 11}
        # part12 -HN
        # HE - 1  # HG - 3
        # HH - 4  # HK - 7
        # HL - 8
        self.part12 = {'HE': 1, 'HG': 3, 'HH': 4, 'HK': 7, 'HL': 8}

        # part13 HO-
        #

    @staticmethod
    def connect_to_db(filename):
        # Открываем файл с секретами
        # Подключаемся к базе данных
        # Возвращает connection
        connection = sqlite3.connect(f'reference/database.db')

        return connection

    def grab_data(self, connection):
        # Берём нужные данные
        # Колонки - константы, их берём с self
        # Возвращает константу с данными data
        pass
