import psycopg2

conn = psycopg2.connect(host='127.0.0.1', database='work_py_db', user='postgres', password='6336')
# Вам необходимо разработать структуру БД для хранения информации и несколько функций на python для управления данными:
#
# Функция, создающая структуру БД (таблицы)
with conn.cursor() as cur:
    cur.execute("""
                DROP TABLE person;
                DROP TABLE telephone;
                """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS telephone(
                 telephone_id SERIAL PRIMARY KEY,
                 number INTEGER UNIQUE
                 );
                 """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS person(
                person_id SERIAL PRIMARY KEY,
                name VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL,
                email VARCHAR(100) NOT NULL,
                telephone_id INTEGER REFERENCES telephone(telephone_id)
                );
                """)
    conn.commit()


    # Функция, позволяющая добавить нового клиента
    def add_person(cursor, name: str, surname: str, email: str):
        cursor.execute("""
                    INSERT INTO person(name, surname, email)
                    VALUES(%s, %s, %s);
                    """, (name, surname, email))



    add_person(cur, 'Kurban', 'Akhmedov', 'malkolm')
    conn.commit()
    # Функция, позволяющая добавить телефон для существующего клиента
    # Функция, позволяющая изменить данные о клиенте
    # Функция, позволяющая удалить телефон для существующего клиента
    # Функция, позволяющая удалить существующего клиента
    # Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
conn.close()
