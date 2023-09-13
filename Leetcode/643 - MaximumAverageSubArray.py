
'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value 
and return this value. Any answer with a calculation error less than 10-5 will be accepted.

'''


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        curr = sum
        for x in range(k, len(nums)):
            sum += nums[x] - nums[x - k]
            curr = max(curr, sum)

        ans = curr / k

        return ans
