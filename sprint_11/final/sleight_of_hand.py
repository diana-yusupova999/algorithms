"""
«Тренажёр для скоростной печати» представляет собой квадратную клавиатуру из шестнадцати клавиш размером 4x4.
На каждой клавише может быть изображена либо точка, либо цифра от 1 до 9.

Занятие на тренажёре делится на раунды:
    - каждый раунд состоит из нескольких игр;
    - в разных раундах число игр может быть разным;
    - номер каждой игры в раунде обозначается счётчиком t.
Для каждого раунда на клавишах устанавливаются определённые значения,
которые остаются неизменными в течение всех игр раунда.

Значение счётчика игр t не может превысить значение самого большого числа, отображённого на клавиатуре в текущем раунде.

В упражнении на тренажёре принимают участие два игрока, они играют вдвоём на одной клавиатуре.
Для каждого раунда устанавливается максимальное число клавиш, которые может нажать один игрок
(оно обозначается переменной k и не изменяется в течение раунда).

В каждой отдельной игре участники должны вместе нажать на клавиши,
на которых изображена цифра, соответствующая номеру игры t.
Например, во второй игре раунда игроки должны нажать все те клавиши, на которых изображена двойка.

В раунде могут быть игры, где не требуется нажимать кнопки.

Задача

Напишите программу, которая будет принимать данные для определённого раунда:

значение k,
значения для кнопок,
и вычислит количество баллов, которое будут заработано в этом раунде.

Формат ввода:
В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках заданы значения для кнопок –— по 4 символа в каждой строке.
Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.

Формат вывода:
Выведите единственное число –— количество баллов, которое игроки наберут в раунде.

Пример 1
Ввод	Вывод
3       2
1231
2..2
2..2
2..2

Пример 2
Ввод	Вывод
4       1
1111
9999
1111
9911

Пример 3
Ввод	Вывод
4       0
1111
1111
1111
1111
"""

import sys
from collections import defaultdict
from typing import List


def count_digits(matrix: List[str]) -> dict:
    num_digits = defaultdict(int)
    for line in matrix:
        for j in range(len(line)):
            if line[j] == '.':
                continue
            num_digits[line[j]] += 1
    return num_digits


def calc_score_of_players(max_keys: int, num_digits: dict) -> int:
    return sum(1 for i in num_digits.values() if i <= max_keys)


def main() -> None:
    players = 2
    max_keys = int(input()) * players
    dimension = 4  # размерность игрового поля
    matrix = []
    for i in range(dimension):
        line = sys.stdin.readline().rstrip()
        matrix.append(line)

    num_digits = count_digits(matrix)
    print(calc_score_of_players(max_keys, num_digits))


if __name__ == '__main__':
    main()
