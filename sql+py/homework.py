import psycopg2


# Функция, создающая структуру БД (таблицы)
def add_tables(cursor):
    cursor.execute("""
                DROP TABLE person;
                DROP TABLE telephone;
                """)
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS telephone(
                 telephone_id SERIAL PRIMARY KEY,
                 number BIGINT UNIQUE
                 );
                 """)

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS person(
                person_id SERIAL PRIMARY KEY,
                name VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL,
                email VARCHAR(100) NOT NULL,
                telephone_id INTEGER REFERENCES telephone(telephone_id)
                );
                """)


# Функция, позволяющая добавить нового клиента
def add_person(cursor):
    print('Введите данные клиента, которого желаете добавить:')
    name = str(input('name:'))
    surname = str(input('surname:'))
    email = str(input('email:'))
    cursor.execute("""
                INSERT INTO person(name, surname, email)
                VALUES(%s, %s, %s);
                """, (name, surname, email))


# Функция, позволяющая добавить телефон для существующего клиента
def add_telephone(cursor):
    print('Введите данные клиента и номер телефона, который желаете добавить для клиента:')
    name = str(input('name:'))
    surname = str(input('surname:'))
    number = str(input('number:'))

    cursor.execute("""
    INSERT INTO telephone(number)
    VALUES( %s );""", (number,))
    #
    cursor.execute("""
                    UPDATE person set telephone_id = (SELECT telephone_id FROM telephone WHERE number=%s ) 
                    WHERE name=%s AND surname=%s ;
                    """, (number, name, surname))


# Функция, позволяющая изменить данные о клиенте
def update_person(cursor):
    print('Введите данные клиента, которого желаете изменить:')
    name = str(input('name:'))
    surname = str(input('surname:'))
    email = str(input('email:'))

    new_name = str(input('name:'))
    new_surname = str(input('surname:'))
    new_email = str(input('email:'))

    #
    cursor.execute("""
                    UPDATE person set name=%s, surname=%s, email=%s 
                    WHERE name=%s AND surname=%s AND email=%s
                    """, (new_name, new_surname, new_email, name, surname, email))


# Функция, позволяющая удалить телефон для существующего клиента
def del_telephone_date(cursor):
    print('Введите данные клиента, номер телефон которого желаете удалить:')
    name = str(input('name:'))
    surname = str(input('surname:'))
    cursor.execute("""
                                select person.telephone_id from
                                person join telephone on person.telephone_id =telephone.telephone_id
                                WHERE name=%s AND surname=%s;
                                """, (name, surname))
    id_number = cursor.fetchone()[0]

    cursor.execute("""
                    UPDATE person SET telephone_id=null WHERE name=%s AND surname=%s ;
                    """, (name, surname))

    cursor.execute("""
                DELETE FROM telephone WHERE telephone_id=%s ; 
                """, (id_number,))


# Функция, позволяющая удалить существующего клиента
def del_person_date(cursor):
    print('Введите данные клиента, которого желаете удалить')
    name = str(input('name:'))
    surname = str(input('surname:'))
    cursor.execute("""
                    DELETE FROM person WHERE name=%s AND surname=%s;
                    """, (name, surname))


# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
def find_person_date(cursor):
    print(
        'Введите данные пользователя, которого хотите найти(данные в котором не уверенны можно отметить пропуском):')
    name = str(input('name:'))
    surname = str(input('surname:'))
    email = str(input('email:'))
    number = str(input('number:'))
    print('Пользователи найденные по вашему запросу')
    cursor.execute("""
                    SELECT * FROM person LEFT JOIN telephone ON person.telephone_id = telephone.telephone_id
                     WHERE name=%s OR surname=%s OR email=%s ;
                    """, (name, surname, email, number))

    return cursor.fetchone()


# print(find_person_date(cur))

if __name__ == '__main__':
    conn = psycopg2.connect(host='127.0.0.1', database='work_py_db', user='postgres', password='6336')
    with conn.cursor() as cur:
        add_tables(cur)
        conn.commit()
    conn.close()
