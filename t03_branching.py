"""Тема 3. Операторы ветвления: if/elif/else, логические операторы, словарь вместо switch."""


def task_13(n):
    """Знак числа.

    Верните 1, если n положительное; -1, если отрицательное; 0, если ноль.

    Примеры:
        task_13(42) == 1
        task_13(-3) == -1
        task_13(0) == 0
    """
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def task_14(score):
    """Оценка по баллам.

    Верните строку с оценкой по 100-балльной шкале:
      90 и выше     — "отлично"
      75–89         — "хорошо"
      60–74         — "удовлетворительно"
      ниже 60       — "неудовлетворительно"

    Примеры:
        task_14(90) == "отлично"
        task_14(89) == "хорошо"
        task_14(60) == "удовлетворительно"
        task_14(59) == "неудовлетворительно"
    """
    if score >= 90:
        return "отлично"
    elif score >= 75:
        return "хорошо"
    elif score >= 60:
        return "удовлетворительно"
    else:
        return "неудовлетворительно"


def task_15(age, is_citizen):
    """Право голоса.

    Человек может голосовать, если ему 18 лет или больше И он является
    гражданином. Верните True или False.

    Примеры:
        task_15(19, True) == True
        task_15(19, False) == False
        task_15(17, True) == False
        task_15(18, True) == True
    """
    return age >= 18 and is_citizen


def task_16(password):
    """Валидный пароль.

    Пароль валиден, если одновременно:
      - его длина не меньше 8 символов;
      - есть хотя бы одна заглавная буква;
      - есть хотя бы одна цифра.
    Верните True или False.

    Примеры:
        task_16("Str0ngPass") == True
        task_16("str0ngpass") == False   # нет заглавной
        task_16("StrongPass") == False   # нет цифры
        task_16("Str1") == False         # короткий
    """
    if len(password) < 8:
        return False
    
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    return has_upper and has_digit


def task_17(year):
    """Високосный год.

    Год високосный, если он делится на 4, но не делится на 100,
    либо делится на 400. Верните True или False.

    Примеры:
        task_17(2024) == True
        task_17(2023) == False
        task_17(1900) == False   # делится на 100, но не на 400
        task_17(2000) == True    # делится на 400
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def task_18(op, a, b):
    """Калькулятор через словарь операций.

    Реализуйте калькулятор, выбирающий операцию по строке op.
    Поддерживаются "+", "-", "*", "/". Верните результат операции.
    Для неизвестной операции и для деления на ноль верните None.
    Рекомендуемый способ — словарь {операция: функция} вместо длинной
    лестницы if/elif (в Python так часто заменяют switch).

    Примеры:
        task_18("+", 2, 3) == 5
        task_18("*", 4, 2.5) == 10.0
        task_18("/", 7, 2) == 3.5
        task_18("/", 5, 0) is None
        task_18("^", 2, 3) is None
    """
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else None
    }
    
    if op in operations:
        return operations[op](a, b)
    else:
        return None