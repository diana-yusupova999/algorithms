"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""
from typing import List


def move_zeroes(nums: List[int]) -> None:
    if len(set(nums)) == 1:
        return None
    nums_len = len(nums)
    i = 0
    while i < nums_len:
        if nums[i] != 0:
            i += 1
            continue
        nums.pop(i)
        nums.append(0)
        nums_len -= 1
    return None
