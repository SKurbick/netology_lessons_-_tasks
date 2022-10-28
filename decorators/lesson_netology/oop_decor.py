class People:
    population = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod  # метод связанный с переменными до функций инициализации внутри класса
    def born(cls, name):
        new_people = cls(name, age=0)
        cls.population.append(new_people)
        return new_people

    @staticmethod  # метод определяющий что функция статична и не связана с переменными внутри класса
    def say_hello():
        print("Hello")

    @property  # метод декоратора класса превращает в вычисляемое свойство
    def passport(self):
        return f"""
        Имя: {self.name}
        Возраст: {self.age}
        """


petr = People.born("Петя")
katerina = People.born("Катя")
print(People.population)
print(petr.passport)
