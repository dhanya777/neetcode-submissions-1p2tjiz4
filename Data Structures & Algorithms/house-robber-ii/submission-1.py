class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_linear(nums, i, end):
            memo = {}

            def solve(i):
                if i > end:
                    return 0

                if i in memo:
                    return memo[i]

                rob_current = nums[i] + solve(i + 2)
                skip_current = solve(i + 1)

                memo[i] = max(rob_current, skip_current)
                return memo[i]

            return solve(i)

        n = len(nums)

        if n == 1:
            return nums[0]

        case1 = rob_linear(nums, 0, n - 2)
        case2 = rob_linear(nums, 1, n - 1)

        return max(case1, case2)
       
  
