class Solution(object):
    def mergeAlternately(self, word1, word2):
        n = len(word1)
        m = len(word2)
        i = 0
        j = 0
        result = ""
        while i < m or j < n:
            if j < n:
                result += word1[j]
                j += 1
            if i < m:
                result += word2[i]
                i += 1

        return "".join(result)