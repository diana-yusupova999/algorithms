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
    max_h = -1
    idx = []
    for i in range(len(height)):
        if height[i] == max_h:
            idx.append(i)
        if height[i] > max_h:
            max_h = height[i]
            idx = [i]
    res = 0
    for i in idx:
        for j in range(len(height)):
            n = math.fabs(i-j)
            tmp = height[j] * n
            if tmp > res:
                res = tmp
    return res


print(max_container([1, 1, 1, 1, 1]))
