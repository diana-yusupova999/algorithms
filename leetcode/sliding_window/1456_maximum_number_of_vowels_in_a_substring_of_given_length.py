"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""


def max_vowels(s: str, k: int) -> int:
    vowels = 'aeiou'
    max_count = 0
    for val in s[:k]:
        if val in vowels:
            max_count += 1
    i = 0
    count = max_count
    while i < len(s) - k:
        if s[i] in vowels:
            count -= 1
        if s[i + k] in vowels:
            count += 1
        if count > max_count:
            max_count = count
            if max_count == k:
                return max_count
        i += 1
    return max_count


print(max_vowels(s='weallloveyou', k=7))
