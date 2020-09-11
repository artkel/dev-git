import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''

    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))

    score = (np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return(score)


def game_core_v2(number):
    count = 1  # счетчик попыток
    number = np.random.randint(1, 101)
    bottom = 0
    up = range(1, 101)[-1]
    predict = int((bottom + up) / 2)

    while number != predict:
        count += 1
        if number > predict:
            bottom = int(predict + 1)
            predict = int((bottom + up) / 2)
        elif number < predict:
            up = int(predict - 1)
            predict = int((bottom + up) / 2)

    return count

score_game(game_core_v2)
