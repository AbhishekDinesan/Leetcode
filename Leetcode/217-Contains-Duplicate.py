'''
**Problem Description:**
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.


For example,
Input: nums = [1,2,3,1]
Output: true

'''

# Approach #1 - Sorting


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False


# Approach #2 - Hashmap

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in numMap:
                return True
            numMap[nums[i]] = i
        return False
