from lib import Database
from lib import Loyalty

database = Database()
connection = database.connect_to_db()
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS rating')
cursor.execute('CREATE TABLE rating (`id` INTEGER, `rating` INTEGER)')

for company_id in range(1, 929 + 1):
    database = Database()
    database.grab_data(connection, company_id)
    data = database.data
    company = database.sort_data(data)

    loyalty = Loyalty(company)
    status = loyalty.check_status()
    if loyalty.score != 0:
        loyalty.check_proceedings()
        loyalty.check_license()
        loyalty.check_special_registers()

    if loyalty.score < 0:
        loyalty.score = 0

    cursor.execute(
        f'INSERT INTO rating VALUES({company[-1]}, {loyalty.score})')

for i in range(1, 17):
    cursor.execute(f'DROP TABLE part{i}')
cursor.close()
connection.commit()
sql = connection.iterdump()

with open('data/output.sql', 'w', encoding='utf-8') as f:
    for line in sql:
        if line.split(' ')[0] == 'CREATE':
            line = line.replace('"', '`')
        elif line.split(' ')[0] == 'INSERT':
            split = line.split('VALUES')
            split[0] = split[0].replace('\"', '`')
            line = 'VALUES'.join(split)

        f.write(line + '\n')
