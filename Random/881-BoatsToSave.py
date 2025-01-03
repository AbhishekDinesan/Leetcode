class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nums.sort()
        ans = 1
        x = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] - x > k:
                x = nums[i]
                ans += 1
        
        return ans
        