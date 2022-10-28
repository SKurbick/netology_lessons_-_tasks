import datetime


def logger(path):
    def _logger(some_func):
        def function(*args, **kwargs):

            date = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
            arguments = f'{args}_{kwargs}'
            name_func = f'{some_func}'
            data =(f'''
            function name: {name_func}
            function arguments: {arguments}      
            date: {date}
                    ''')
            result = some_func(*args, **kwargs)
            file = open(path, "w")
            file.write(data)
            return result

        return function

    return _logger
