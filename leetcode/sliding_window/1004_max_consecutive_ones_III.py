"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""
from typing import List


def longest_ones(nums: List[int], k: int) -> int:
    if k == len(nums):
        return len(nums)

    if len(set(nums)) == 1:
        return len(nums) * nums[0]

    zeroes = []
    for i, val in enumerate(nums):
        if not val:
            zeroes.append(i)

    if len(zeroes) <= k:
        return len(nums)

    max_len = max(zeroes[k], (len(nums) - zeroes[-k - 1] - 1))
    for i in range(len(zeroes) - k - 1):
        len_tmp = zeroes[i + k + 1] - zeroes[i] - 1
        if len_tmp > max_len:
            max_len = len_tmp

    return max_len
