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

print("Бинарный поик:")
def binary_search(number):
    '''Бинарный поик: Предиктор каждую попытку равен середине диапазона поиска;
    при этом каждый раз исключается половина оставшихся чисел'''

    count = 1  # счетчик попыток
    number = np.random.randint(1, 101) # загадываем случайное число в диапазоне от 1 до 100
    bottom = 0 # нижняя граница интревала; изначально равна 0
    up = range(1, 101)[-1] # верхняя граница интрвала; изначально равна 100
    predict = int((bottom + up) / 2) # предиктор - в середине диапазона, изначально 50

    while number != predict:
        count += 1 # до тех пор пока не угадали число, считаем попытки
        if number > predict:
            bottom = int(predict + 1) # если число больше предиктора, отбрасываем половину чисел до предиктора
            predict = int((bottom + up) / 2) # новый предиктор - середина нового диапазона
        elif number < predict:
            up = int(predict - 1) # если число меньше предиктора, отбрасываем половину чисел после предиктора
            predict = int((bottom + up) / 2) # новый предиктор - середина нового диапазона

    return count, # если число угадано, возвращаем счетчик попыток


score_game(binary_search)
