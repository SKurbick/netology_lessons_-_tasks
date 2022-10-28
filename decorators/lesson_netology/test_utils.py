def cached(cache_size):  # дополнительная функция для вычисления опр. аргумента
    def _cached(old_function):  # функция в аргументе которой будет передаваться функция под декоратором
        CACHE = {}  # словарь который будет использован для удобства хранения и обращения к данным
        numbers_of_calls = 0  # переменная для примера

        def new_function(*args, **kwargs):  # аргументы функции под декоратором
            nonlocal numbers_of_calls  # определяет что данные переменной выше можно ИЗМЕНЯТЬ
            numbers_of_calls += 1  # без вызова nonlocal выше сработала бы ошибка на это действие
            result = old_function(*args, **kwargs)  # значения для ключа
            key = f'{args}_{kwargs}'  # ключ
            if key in CACHE:  # если этот ключ уже там имеется
                return CACHE[key]  # выведет данные со словаря

            CACHE[key] = result  # привязывает данные к ключу
            if len(CACHE) > cache_size:  # ограничение для хранения информации
                CACHE.popitem()  # удаление последнего элемента
            print(len(CACHE))  # вывод актуального количества
            return result  # содержание функции

        return new_function  # вызов функции принципиально без скобок для корректного декорирования

    return _cached  # то же самое
