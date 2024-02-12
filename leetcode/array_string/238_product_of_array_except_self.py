"""
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    i = 0
    while i < len(nums) - 1:
        res[i + 1] = nums[i] * res[i]
        i += 1
    while i > 0:
        nums[i - 1] *= nums[i]
        res[i - 1] *= nums[i]
        i -= 1
    return res
