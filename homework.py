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
                 number DECIMAL UNIQUE
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


    add_person(cur, 'Kurban', 'Akhmedov', 'malkolm.63.zed@mail.ru')
    conn.commit()


    # Функция, позволяющая добавить телефон для существующего клиента
    def add_telephone(cursor, number, name, surname):
        cursor.execute("""
        INSERT INTO telephone(number)
        VALUES( %s );""", (number,))
        #
        cursor.execute("""
                        UPDATE person set telephone_id = (SELECT telephone_id FROM telephone WHERE number=%s ) 
                        WHERE name=%s AND surname=%s ;
                        """, (number, name, surname))

        conn.commit()


    add_telephone(cur, '89640206389', 'Kurban', 'Akhmedov')


    # Функция, позволяющая изменить данные о клиенте
    def update_person(cursor, name: str, surname: str, mail: str):
        pass


    #
    #     cursor.execute("""
    #                     UPDATE person set
    #                     """)

    # Функция, позволяющая удалить телефон для существующего клиента
    def del_telephone_date(cursor, name, surname):
        cursor.execute("""
                                    select person.telephone_id from
                                    person join telephone on person.telephone_id =telephone.telephone_id
                                    WHERE name=%s AND surname=%s;
                                    """, (name, surname))
        id_number = cur.fetchone()[0]

        cursor.execute("""
                        UPDATE person SET telephone_id=null WHERE name=%s AND surname=%s ;
                        """, (name, surname))

        cursor.execute("""
                    DELETE FROM telephone WHERE telephone_id=%s ; 
                    """, (id_number,))
        print(id_number)

        conn.commit()


    # del_telephone_date(cur, 'Kurban', 'Akhmedov')

    # Функция, позволяющая удалить существующего клиента
    def del_person_date(cursor, name, surname):
        cursor.execute("""
                        DELETE FROM person WHERE name=%s AND surname=%s;
                        """, (name, surname))

        conn.commit()


    # del_person_date(cur,'Kurban', 'Akhmedov')

    # Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
    def find_person_date():
        pass
conn.close()
