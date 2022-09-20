import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

"""СОЗДАЮТСЯ ТАБЛИЦЫ АНАЛОГИЧНО SQL-ЗАПРОСАМ"""


class Course(Base):
    __tablename__ = "course"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    # homeworks = relationship("Homework", back_populates="course")

    def __str__(self):
        return f'Course {self.id}: {self.name}'


class Homework(Base):
    __tablename__ = "homework"

    id = sq.Column(sq.Integer, primary_key=True)
    number = sq.Column(sq.Integer, nullable=False)
    description = sq.Column(sq.Text, nullable=False)
    course_id = sq.Column(sq.Integer, sq.ForeignKey("course.id"), nullable=False)

    # course = relationship(Course, back_populates="homeworks")
    course = relationship(Course,
                          backref="homeworks")  # с помощью этой переменной мы связывем с id Course (foreign key)

    def __str__(self):
        return f'Homework {self.id}: ({self.number}, {self.description}, {self.course_id})'


def create_tables(engine):
    Base.metadata.drop_all(engine)  # удаление таблиц
    Base.metadata.create_all(engine)  # создание таблиц
