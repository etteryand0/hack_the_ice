import sqlite3


class Database:
    def __init__(self):
        # Обозначаем нужные константы - колонки
        # part1 A-P
        # B - 1
        # D - 3
        self.parts = {'B': 1, 'D': 3, 'AL': 6, 'AM': 7,
                      'AR': 12, 'BV': 2, 'BY': 5, 'CE': 11,
                      'HE': 1, 'HG': 3, 'HH': 4, 'HK': 7,
                      'HL': 8, 'A': 0}
        # part3 AG-BR
        # AL - 6  # AM - 7
        # AR - 12

        # part5 BU-
        # BV - 2  # BY - 5
        # CE - 11

        # part12 -HN
        # HE - 1  # HG - 3
        # HH - 4  # HK - 7
        # HL - 8W

        self.data = {'B': None, 'D': None, 'AL': None, 'AM': None,
                     'AR': None, 'BV': None, 'BY': None, 'CE': None,
                     'HE': None, 'HG': None, 'HH': None, 'HK': None,
                     'HL': None, 'A': None}
        self.structure = [(1, ['A', 'B', 'D']), (3, ['AL', 'AM', 'AR']),
                          (5, ['BV', 'CE', 'BY']), (12, ['HK', 'HL', 'HH', 'HG', 'HE'])]

    @staticmethod
    def connect_to_db():
        # Открываем файл с секретами
        # Подключаемся к базе данных
        # Возвращает connection
        connection = sqlite3.connect(f'data/database.db')

        return connection

    def grab_data(self, connection, company_id):
        # Берём нужные данные
        # Колонки - константы, их берём с self
        # Возвращает константу с данными data
        cursor = connection.cursor()

        for index in [(1), (3), (5), (12)]:
            cursor.execute(f'SELECT * FROM part{index} WHERE id={company_id}')
            data = cursor.fetchone()

            for key in self.structure[0][1]:
                i = self.parts[key]
                self.data[key] = data[i]
                # print(self.data[key])

            self.structure.pop(0)

        cursor.close()
        return True

    @staticmethod
    def sort_data(data):
        company = []
        for key in ['B', 'D', 'AL', 'AM', 'BV', 'CE', 'BY',
                    'AR', 'HK', 'HL', 'HH', 'HG', 'HE', 'A']:
            company.append(data[key])
        # print(company)
        return company
