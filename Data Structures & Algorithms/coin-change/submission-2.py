from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @lru_cache(None)
        mem={}
        def solve(rem):
            if rem==0:
                return 0
            if rem<0:
                return float('inf')
            min_coins=float('inf')
            if rem in mem:
                return mem[rem]

            for coin in coins:
                result=solve(rem-coin)
                min_coins=min(min_coins,result+1)
            mem[rem]=min_coins
            return mem[rem]

        result=solve(amount)
        return result if result!=float('inf') else -1

        