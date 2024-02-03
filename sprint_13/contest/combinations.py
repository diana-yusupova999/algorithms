# from typing import List
#
#
# def combination(comb: str, selected_letters: List[str], index: int, count: int, result: List[str]):
#     if index == 3:
#         result.append(comb)
#         return result
#
#     combination(comb + selected_letters[index][count], selected_letters, 0, [])
#     combination(comb + selected_letters[index][count + 1], selected_letters, 0, [])
#     combination(comb + selected_letters[index][count + 2], selected_letters, 0, [])
#
#
# if __name__ == '__main__':
#     button = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
#     number_sequence = input()
#     selected_letters = [button[i] for i in number_sequence]
#     result = combination('', selected_letters, 0, [])
#     print(*result)

def findCombinations(keypad, keys, combinations, index, result=''):
    # если мы обработали каждую цифру ключа, вывести результат
    if index == -1:
        combinations.add(result)
        return

    # сохраняет текущую цифру
    digit = keys[index]

    # получить размер списка, соответствующий текущей цифре
    length = len(keypad[digit])

    # одну за другой замените цифру на каждый символ в соответствующем
    # Список # и повторение для следующей цифры
    for i in range(length):
        findCombinations(keypad, keys, combinations, index - 1, keypad[digit][i] + result)


def findAllCombinations(keypad, keys):
    # неверный ввод - вернуть пустой набор
    if not keypad or not keys:
        return set()

    # настроен на сохранение всех комбинаций
    combinations = set()

    # найти и вернуть все комбинации
    findCombinations(keypad, keys, combinations, len(keys) - 1)
    return combinations


if __name__ == '__main__':
    # Мобильная клавиатура
    keypad = {
        # 0 и 1 цифры не имеют связанных символов
        2: ['a', 'b', 'b'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }

    # ввод номера в виде списка (номер не может начинаться с 0 или 1)
    keys_input = input()
    keys = [int(i) for i in keys_input]

    # найти все комбинации
    combinations = findAllCombinations(keypad, keys)
    print(*combinations)
