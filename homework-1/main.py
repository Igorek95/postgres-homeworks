import psycopg2
import csv

# Считываем пароль для подключения к базе данных из файла
password_db = open("/home/garik/PycharmProjects/postgres-homeworks2/password_db.txt").read().strip()

# Считываем данные из CSV-файла
with open('/home/garik/PycharmProjects/postgres-homeworks2/homework-1/north_data/customers_data.csv', newline='') as csvfile:
    data_reader = csv.reader(csvfile)
    next(data_reader)  # Пропускаем заголовок, если он есть

    # Подключаемся к базе данных
    with psycopg2.connect(host='localhost', database='north', user='postgres', password='1234') as conn:
        with conn.cursor() as cur:
            for row in data_reader:
                # Преобразуем данные из CSV в кортеж и вставляем их в базу данных
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', tuple(row))

            # Выполняем запрос на выборку данных
            cur.execute('SELECT * FROM customers')

            rows = cur.fetchall()
            for row in rows:
                print(row)

# Закрываем соединение с базой данных
conn.close()
