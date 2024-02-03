import sys
from typing import List


def binary_search(arr: List[str], x: int, left: int, right: int):
    if right == left == len(arr):
        return -1

    if right == left and int(arr[right]) >= x:
        return right + 1

    if right <= left:
        return -1

    mid = (left + right) // 2

    if int(arr[mid]) >= x:
        if int(arr[mid - 1]) >= x:
            return binary_search(arr, x, left, mid)
        return mid + 1
    elif x < int(arr[mid]):
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)


if __name__ == '__main__':
    day_count = int(input())
    money_box = sys.stdin.readline().rstrip().split(' ')
    price = int(input())
    res = [binary_search(money_box, price, 0, len(money_box)), binary_search(money_box, price * 2, 0, len(money_box))]
    print(*res)
