'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

For Example,
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''

# Approach #1 - Double Placeholder


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        x = 1
        for i in range(1, length):
            if nums[i] != nums[i - 1]:
                nums[x] = nums[i]
                x += 1
        return x
