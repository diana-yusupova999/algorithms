# ID 88828674
import sys


def partition(members, left, right):
    index_pivot = (left + right) // 2
    pivot = members[index_pivot]
    while left < right:
        while members[left] < pivot:
            left += 1

        while members[right] > pivot:
            right -= 1

        if members[left] == pivot:
            index_pivot = right
        elif members[right] == pivot:
            index_pivot = left
        members[left], members[right] = members[right], members[left]
    return index_pivot


def quick_sort(members, left, right):
    if (right - left) > 0:
        index_pivot = partition(members, left, right)
        quick_sort(members, left, index_pivot)
        quick_sort(members, index_pivot + 1, right)


def transformation(input_data: list) -> list:
    name, score, fail = input_data
    return [-int(score), int(fail), name]


def main() -> None:
    n = int(input())
    members = [transformation(sys.stdin.readline().rstrip().split(' ')) for i in range(n)]

    quick_sort(members, 0, len(members) - 1)
    for score, fail, name in members:
        print(name)


if __name__ == '__main__':
    main()
