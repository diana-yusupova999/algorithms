"""
Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить,
имеет длину n, то есть состоит из n одинаковых идущих подряд участков.
Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка.
Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы.
Дома в городе Тимофея нумеровались в том порядке, в котором строились,
поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

Формат ввода:
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106).
В следующей строке записаны n целых неотрицательных чисел — номера домов и
обозначения пустых участков на карте (нули).
Гарантируется, что в последовательности есть хотя бы один ноль.
Номера домов (положительные числа) уникальны и не превосходят 109.

Формат вывода:
Для каждого из участков выведите расстояние до ближайшего нуля.
Числа выводите в одну строку, разделяя их пробелами.

Пример 1
Ввод	              Вывод
5
0 1 4 9 0             0 1 2 1 0

Пример 2
Ввод	              Вывод
6
0 7 9 4 8 20          0 1 2 3 4 5
"""

from typing import List
import sys


def find_zeros_indexes(street: List[str]) -> List[int]:
    zeros_indexes = []
    for i in range(len(street)):
        if street[i] == '0':
            zeros_indexes.append(i)

    return zeros_indexes


def distance_search(street: List[str], zeros_indexes: List[int]) -> List[str]:
    if len(zeros_indexes) == 1:
        result = [str(abs(i - zeros_indexes[0])) for i in range(len(street))]
        return result

    result = ['0'] * len(street)

    for count, zero_index in enumerate(zeros_indexes):
        if count == 0 and zero_index != 0:
            index = zero_index
            while index > -1:
                result[index] = str(zero_index - index)
                index -= 1
        elif (count == len(zeros_indexes) - 1) and (zero_index != len(result) - 1):
            index = zero_index
            while index < len(result):
                result[index] = str(index - zero_index)
                index += 1
            continue

        if count == len(zeros_indexes) - 1:
            continue

        left_index = zero_index + 1
        right_index = zeros_indexes[count + 1] - 1
        while left_index <= right_index:
            result[left_index] = str(left_index - zero_index)
            result[right_index] = str(zeros_indexes[count + 1] - right_index)
            left_index += 1
            right_index -= 1

    return result


def main() -> None:
    n = int(input())
    line = sys.stdin.readline().rstrip()
    street = line.split()
    zeros_indexes = find_zeros_indexes(street)
    print(' '.join(distance_search(street, zeros_indexes)))


if __name__ == '__main__':
    main()
