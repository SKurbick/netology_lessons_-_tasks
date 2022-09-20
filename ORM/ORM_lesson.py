import sqlalchemy  # модуль для работы с SQL таблицами (в нашем случае  postgresql) через ORM
from sqlalchemy.orm import sessionmaker

from ORM.models_lesson import create_tables, Course, \
    Homework  # импортирует модули классов и функцию для создания таблиц

DSN = 'postgresql://postgres:6336@localhost:5432/work_py_db'
# указываем используемую СУБД, пользователя, пароль к нему, хост, порт и саму БД

engine = sqlalchemy.create_engine(DSN)  # создаем абстракцию для подключения к БД

create_tables(engine)  # создаем таблицу самописной функцией

Session = sessionmaker(bind=engine)
session = Session()  # открываем сессию для работы с БД, с помощью же неё мы будем реализовывать все манипуляции с БД

# создаем данные для таблицы
course1 = Course(name="Python")
course2 = Course(name="Java")
# print(course1.id)

session.add_all([course1, course2])  # добавляем данные в таблицу пользуясь "сессией"
session.commit()  # комитим что бы сохранить изменения в таблицу

# print(course1.id)
# print(course1)

# создаем данные для таблицы
hm1 = Homework(number=1, description="простая домашняя работа", course=course1)
hm2 = Homework(number=2, description="сложная домашняя работа", course=course1)
session.add_all([hm1, hm2])
session.commit()

# for hm in session.query(Homework).filter(Homework.number > 1).all(): #  благодаря query() мы можем "извлекать" данные,
# а с помощью filter() мы задали извлекаемое значение
# в query() указан модель класса с которого будем извлекать
for hm in session.query(Homework).filter(Homework.description.like("%прост%")).all():
    # как и в sql можно использовать метод like() для сравнения
    print(hm)

for c in session.query(Course).join(Homework.course).filter(Homework.number == 2).all():
    # извлекаем данные из Course соединяя при этом таблицы с HW используя оператор сравнения, где на выходе получим ответ
    # касающийся таблицы Course. Аналогично SQL
    print(c)

subq = session.query(Homework).filter(Homework.description.like('%сложн%')).subquery()#создаем подзапрос
for course in session.query(Course).join(subq, Course.id == subq.c.course_id).all():
    print(course)

session.query(Course).filter(Course.name == 'Java').update(({'name': 'JavaScript'}))# изменение данных
session.commit()

session.query(Course).filter(Course.name == 'JavaScript').delete() # удаление данных
session.commit()

session.close()
