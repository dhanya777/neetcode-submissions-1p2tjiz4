from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def solve(rem):
            if rem==0:
                return 0
            if rem<0:
                return float('inf')
            min_coins=float('inf')

            for coin in coins:
                result=solve(rem-coin)
                min_coins=min(min_coins,result+1)
            return min_coins

        result=solve(amount)
        return result if result!=float('inf') else -1

        