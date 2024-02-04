"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""


def gcd_of_strings(str1: str, str2: str) -> str:
    if set(str1) != set(str2):
        return ''

    common_div = len(set(str1))
    longest_common_div = len(set(str1))
    l1 = len(str1)
    l2 = len(str2)
    while common_div <= min(l1, l2):
        if l1 % common_div == 0 and l2 % common_div == 0:
            if longest_common_div < common_div:
                longest_common_div = common_div
        common_div += 1

    check_1 = str1[:longest_common_div] * (l1 // longest_common_div)
    check_2 = str1[:longest_common_div] * (l2 // longest_common_div)
    if check_1 != str1 or check_2 != str2:
        return ''
    return str1[:longest_common_div]
