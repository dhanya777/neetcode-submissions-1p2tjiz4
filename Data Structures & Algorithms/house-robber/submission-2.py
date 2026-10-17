class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def solve(i):
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            rob_current=nums[i]+solve(i+2)
            skip_current=solve(i+1)

            memo[i]= max(rob_current,skip_current)
            return memo[i]
        return solve(0)

        