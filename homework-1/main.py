import psycopg2
import csv

# Считываем пароль для подключения к базе данных из файла
password_db = open("/home/garik/PycharmProjects/postgres-homeworks2/password_db.txt").read().strip()


def add_db(path_file, name_table):
    try:
        with open(path_file,
                  newline='') as csvfile:
            data_reader = csv.reader(csvfile)
            header = next(data_reader)  # Получаем заголовок
            data_list = []
            for row in data_reader:
                data_list.append(tuple(row))

            # Подключаемся к базе данных
            with psycopg2.connect(host='localhost', database='north', user='postgres', password='1234') as conn:
                with conn.cursor() as cur:
                    # Создаем строку SQL для вставки данных
                    columns = ', '.join(header)
                    placeholders = ', '.join(['%s'] * len(header))
                    sql = f'INSERT INTO {name_table} ({columns}) VALUES ({placeholders})'

                    # Вставляем данные в базу данных
                    cur.executemany(sql, data_list)

    finally:
        # Закрываем соединение с базой данных
        conn.close()


if __name__ == '__main__':
    add_db('north_data/customers_data.csv', 'customers')
    add_db('north_data/employees_data.csv', 'employees')
    add_db('north_data/orders_data.csv', 'orders')
