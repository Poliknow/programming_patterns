"""Домашнее задание. Тема 3: декораторы. (решение)"""

import functools


def hw_08(func):
    """Декоратор once.

    Первый вызов декорированной функции возвращает её результат.
    Каждый последующий вызов возбуждает RuntimeError с сообщением,
    содержащим слово "уже".

    Примеры:
        @hw_08
        def init(): return 42

        init() == 42
        init()  # RuntimeError ... уже ...
    """
    called = False

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal called
        if called:
            raise RuntimeError("Функция уже была вызвана")
        called = True
        return func(*args, **kwargs)

    return wrapper


def hw_09(*types):
    """Фабрика декораторов require_types.

    hw_09(T1, T2, ...) возвращает декоратор, проверяющий, что каждый
    позиционный аргумент вызова — экземпляр соответствующего типа
    (первый аргумент — T1, второй — T2 и т.д.; лишние аргументы не проверяются).
    При несоответствии — TypeError с сообщением, содержащим слово "тип".
    Иначе — результат исходной функции.

    Примеры:
        @hw_09(str, int)
        def greet(name, age): return f"{name}, {age}"

        greet("Анна", 30) == "Анна, 30"
        greet("Анна", "30")    # TypeError ... тип ...
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for index, expected_type in enumerate(types):
                if index >= len(args):
                    break
                if not isinstance(args[index], expected_type):
                    raise TypeError(
                        f"Неверный тип аргумента #{index + 1}: "
                        f"ожидался {expected_type.__name__}, "
                        f"получен {type(args[index]).__name__}"
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator


def hw_10(func):
    """Декоратор trace.

    Обёртка ведёт журнал вызовов: атрибут log — список кортежей позиционных
    аргументов каждого вызова (в порядке вызовов). Результат вызова
    пробрасывается. Именованные аргументы в журнал не пишутся.

    Примеры:
        @hw_10
        def add(a, b): return a + b

        add.log == []
        add(1, 2) == 3
        add(3, 4) == 7
        add.log == [(1, 2), (3, 4)]
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.log.append(args)
        return func(*args, **kwargs)

    wrapper.log = []
    return wrapper
