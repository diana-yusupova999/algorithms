"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""
import math
from typing import List


def max_container(height: List[int]) -> int:
    left_idx = 0
    right_idx = len(height) - 1
    max_val = 0

    while left_idx < right_idx:
        cur_val = min(height[left_idx], height[right_idx]) * (right_idx - left_idx)
        max_val = max(max_val, cur_val)
        if height[left_idx] < height[right_idx]:
            left_idx += 1
        else:
            right_idx -= 1
    return max_val


print(max_container([1,8,6,2,5,4,8,3,7]))
