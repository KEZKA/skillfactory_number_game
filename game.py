"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Поскольку 2^7 уже больше чем 100, будем использовать бинарный поиск

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = 50  # Задаем начальное значение для предпологаемого числа
    step = 50  # Задаем начальный шаг между попытками
    while True:
        count += 1
        if step > 1:
            # Делим шаг на цело на 2, если число не четное, то округляем в большую сторону
            step = step//2 if step % 2 == 0 else step//2+1
            # Если не накладывать это условие - максимальное кол-во попыток будет 9, что тоже нам подходит
        # Сравниваем наше число с загаданным и в зависимости от результата увеличивем число на шаг или уменьшаем
        if number > predict_number:
            predict_number += step
        elif number < predict_number:
            predict_number -= step
        else:  # Если условия на > и < оказались неверны, то числа равны
            return count  # Выходим из функции, возвращаем кол-во попыток


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(
        f"Ваш алгоритм угадывает число в среднем за:{score} попыток, максимальное кол-во попыток {max(count_ls)}")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
