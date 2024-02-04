"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""


def reverse_vowels(s: str) -> str:
    """
    :type s: str
    :rtype: str
    """
    s_list = list(s)
    vowels = 'aeiouAEIOU'
    l_i = 0
    r_i = len(s) - 1
    while l_i < r_i:
        if s_list[l_i] in vowels and s_list[r_i] in vowels:
            s_list[l_i], s_list[r_i] = s_list[r_i], s_list[l_i]
            l_i += 1
            r_i -= 1
            continue

        while s_list[l_i] not in vowels and l_i < r_i:
            l_i += 1

        while s_list[r_i] not in vowels and l_i < r_i:
            r_i -= 1

    s = ''.join(s_list)
    return s
