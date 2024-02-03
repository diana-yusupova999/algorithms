# iD 88809864
from typing import List


def broken_search(nums: List[int], target: int) -> int:
    left_index = 0
    right_index = len(nums) - 1
    while right_index >= left_index:
        middle_index = (left_index + right_index) // 2
        if nums[middle_index] == target:
            return middle_index
        if nums[left_index] == target:
            return left_index
        if nums[right_index] == target:
            return right_index

        if nums[left_index] < nums[middle_index]:
            if nums[left_index] < target < nums[middle_index]:
                right_index = middle_index - 1
                left_index += 1
            else:
                left_index = middle_index + 1
                right_index -= 1
        else:
            if nums[middle_index] < target < nums[right_index]:
                left_index = middle_index + 1
                right_index -= 1
            else:
                right_index = middle_index - 1
                left_index += 1
    return -1


if __name__ == '__main__':
    def test():
        arr = [8, 10, 0, 2, 4]
        assert broken_search(arr, 4) == 4

    test()
