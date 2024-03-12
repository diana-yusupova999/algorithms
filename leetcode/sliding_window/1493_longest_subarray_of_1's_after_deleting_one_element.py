"""
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
"""
from typing import List


def longest_subarray(nums: List[int]) -> int:
    k = 1
    if k == len(nums):
        return 0

    if len(set(nums)) == 1:
        if nums[0]:
            return len(nums) - 1
        return 0

    zeroes = []
    for i, val in enumerate(nums):
        if not val:
            zeroes.append(i)

    if len(zeroes) <= k:
        return len(nums) - 1

    max_len = max(zeroes[k], (len(nums) - zeroes[-k - 1] - 1))
    for i in range(len(zeroes) - k - 1):
        len_tmp = zeroes[i + k + 1] - zeroes[i] - 1
        if len_tmp > max_len:
            max_len = len_tmp

    return max_len - 1