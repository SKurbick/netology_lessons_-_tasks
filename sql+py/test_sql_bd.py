import psycopg2

conn = psycopg2.connect(host="127.0.0.1", database="netology_db_py", user="postgres", password="6336")
"""Выполнение SQL-запросов
Теперь можно взаимодействовать с БД:
cur.execute() — выполнить одну команду
cur.executemany() — выполнить несколько команд
cur.fetchone() — получить одну строку
cur.fetchmany() — получить несколько строк
cur.fetchall() — получить все строкиSQL"""

with conn.cursor() as cur:
    # cur.execute("""
    # DROP TABLE homework;
    # DROP TABLE course;
    # """)
    cur.execute("""
            CREATE TABLE IF NOT EXISTS course(
                id SERIAL PRIMARY KEY,
                name VARCHAR(40) UNIQUE 
                );
                """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS homework(
                id SERIAL PRIMARY KEY,
                number INTEGER NOT NULL,
                description TEXT NOT NULL,
                course_id INTEGER NOT NULL REFERENCES course(id)
                );
                """)
    conn.commit()  # фиксириуем изменения в БД

    # наполнение таблиц (C из CRUD)
    # cur.execute("""
    #             INSERT INTO course(name) VALUES('Python');
    #             """)
    # conn.commit()  # фиксируем в БД

    # cur.execute("""
    #             INSERT INTO course(name) VALUES('Java') RETURNING id, name;
    #             """)
    # # conn.commit()
    # print(cur.fetchone())  # запрос данных автоматически зафиксирует изменения

    # cur.execute("""
    #             INSERT INTO homework(number, description, course_id)
    #             VALUES(1, 'simple HM', 16);
    #             """)
    # conn.commit()
    #
    # извлечение данных (R из CRUD)
    # cur.execute("""
    #             SELECT * FROM course;
    #             """)
    # print('fetchall', cur.fetchall())  # извлечь все строки
    #
    # cur.execute("""
    #             SELECT * FROM course;
    #             """)
    # print(cur.fetchone())  # извлечь первую строку (аналог LIMIT 1)
    #
    # cur.execute("""
    #             SELECT * FROM course;
    #             """)
    # print(cur.fetchone(3))  # извлечь первые N строк (аналог LIMIT N)
    #
    # cur.execute("""
    #             SELECT id FROM course WHERE name='{}';
    #             """.format('Python'))  # плохо - возможно SQL инъекция
    # print(cur.fetchone())
    #
    # cur.execute("""
    #             SELECT id FROM course WHERE name=%s;
    #             """, ("Java",))  # хорошо
    # print(cur.fetchone())
    #

    def get_course_id(cursor, name: str) -> int:
        cursor.execute("""
                    SELECT id FROM course WHERE name=%s;
                    """, (name,))
        return cur.fetchone()[0]
    #
    #
    java_id = get_course_id(cur, 'Java Advanced')
    print('java_id:', java_id)
    #
    # cur.execute("""
    #             INSERT INTO homework(number, description, course_id)
    #             VALUES(%s, %s, %s);
    #             """, (2, "harder HM", java_id))
    # conn.commit()  # фиксируем в БД
    #
    # cur.execute("""
    #             SELECT * FROM homework;
    #             """)
    # print(cur.fetchall())
    #
    # # обновление данных (U из CRUD)
    # cur.execute("""
    #             UPDATE course SET name=%s WHERE id=%s;
    #             """, ('Java Advanced', java_id))
    # cur.execute("""
    #             SELECT * FROM course;
    #             """)
    # conn.commit()
    # print(cur.fetchall())
    #
    # # удаление данных (D из CRUD)
    cur.execute("""
                DELETE FROM homework WHERE id=%s;
                """, (2,))
    cur.execute("""
                SELECT * FROM homework;
                """)
    print(cur.fetchall())  # запрос данных автоматически зафиксирует изменения

conn.close()
