import sys


def sort_count(input_list: str, len_input: int, max_val: int) -> str:
    if len_input == 0:
        return ''

    counter = [0] * max_val
    for i in input_list:
        if i == '0':
            counter[0] += 1
        elif i == '1':
            counter[1] += 1
        elif i == '2':
            counter[2] += 1

    return '0' * counter[0] + '1' * counter[1] + '2' * counter[2]


if __name__ == '__main__':
    len_input = int(input())
    input_list = sys.stdin.readline().rstrip()
    max_val = 3

    print(*sort_count(input_list, len_input, max_val))
