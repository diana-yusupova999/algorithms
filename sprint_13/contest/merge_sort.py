def merge(arr: list, left: int, mid: int, right: int) -> list:
    result = []
    r = mid
    while (left < mid) and (r < right):
        if arr[left] <= arr[r]:
            result.append(arr[left])
            left += 1
        else:
            result.append(arr[r])
            r += 1

    while left < mid:
        result.append(arr[left])
        left += 1

    while r < right:
        result.append(arr[r])
        r += 1

    return result


def merge_sort(arr: list, left: int, right: int):
    if len(arr[left: right]) < 2:
        return arr
    med = (right - left) // 2 + left
    arr = merge_sort(arr, left, med)
    arr = merge_sort(arr, med, right)

    arr[left: right] = merge(arr, left, med, right)
    return arr


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
