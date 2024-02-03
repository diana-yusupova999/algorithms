"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""


def is_sub_sequence(s: str, t: str) -> bool:
    if not set(s).issubset(set(t)):
        return False
    if len(set(s)) == 0:
        return True
    i = 0
    for val in t:
        if val == s[i]:
            i += 1
        if i == len(s):
            return True
    return False
