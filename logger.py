import datetime


def logger(old_function):
    def new_function(*args,**kwargs):
        print(f'Вызвана функция : {old_function.__name__} с аргументами {args} и {kwargs}')
        print(f'Время вызова функции: {datetime.datetime.now()}')

        result = old_function(*args,**kwargs)
        print( f'Результат : {result}')
        return result

    return new_function
