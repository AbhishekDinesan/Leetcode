
'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Two Pointer pattern

'''


def isSubsequence(self, s: str, t: str) -> bool:
    i = 0
    j = 0
    slen = len(s)
    tlen = len(t)
    while (i < slen & j < tlen):
        if (s[i] == t[i]):
            i += 1
        j += 1
    if (i == slen):
        return true
    return false
