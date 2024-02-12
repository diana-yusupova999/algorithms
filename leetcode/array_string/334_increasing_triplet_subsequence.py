"""
Given an integer array nums, return true if there exists a triple of
indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""
from typing import List


def increasing_triplet(nums: list[int]) -> bool:
    if len(set(nums)) < 3:
        return False
    i = 0
    j = 1
    k = 2
    len_nums = len(nums)
    while (i < len_nums - 2) and (j < len_nums - 1) and (k < len_nums):
        while (j < len_nums - 2) and (nums[i] >= nums[j]):
            j += 1
            k = j + 1

        while (k < len_nums - 1) and (nums[j] >= nums[k] or j >= k):
            k += 1

        if (i < j < k) and (nums[i] < nums[j] < nums[k]):
            return True
        elif j < len_nums - 2:
            j += 1
            k = j + 1
        else:
            i += 1
            j = i + 1
            k = i + 2
    return False
