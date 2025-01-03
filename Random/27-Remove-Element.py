# testing git

'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

For example,

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for x in nums:
            if x != val:
                nums[counter] = x
                counter += 1
        return counter
