"""
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""

from collections import Counter


# count = Counter(nums)
# extract_count = Counter()
# i = 0
# while i < len(nums):
#     if nums[i] in extract_count.keys():
#         extract_count[nums[i]] -= 1
#         if extract_count[nums[i]] == 0:
#             extract_count.pop(nums[i])
#         nums.pop(i)
#         continue
#     val = k - nums[i]
#     if val in count.keys() and count[val] > 0:
#         if val == nums[i] and count[val] < 2:
#             i += 1
#             continue
#         pars += 1
#         count[nums[i]] -= 1
#         count[val] -= 1
#         nums.pop(i)
#         extract_count[val] += 1
#         continue
#     i += 1
def pick_sum(nums: list, k: int) -> int:
    pars = 0
    nums.sort()
    l_i = 0
    r_i = len(nums) - 1
    while l_i < r_i:
        if nums[l_i] + nums[r_i] == k:
            pars += 1
            nums.pop(r_i)
            nums.pop(l_i)
            r_i -= 2
        while l_i < r_i and nums[l_i] + nums[r_i] > k:
            r_i -= 1
        while l_i < r_i and nums[l_i] + nums[r_i] < k:
            l_i += 1
    return pars


n_2 = [1, 1, 1, 2, 2, 2, 3, 4]
n = [3, 1, 3, 4, 3]
print(pick_sum(nums=n, k=6))
print(n)
