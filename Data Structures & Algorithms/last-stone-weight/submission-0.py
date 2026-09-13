import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap=[]

        for stone_wt in stones:
            heapq.heappush(self.heap,-stone_wt)

        while len(self.heap)>1:
            x=-heapq.heappop(self.heap)
            y=-heapq.heappop(self.heap)

            if x==y:
                continue
            elif x>y:
                heapq.heappush(self.heap,-(x-y))
        return -self.heap[0] if self.heap else 0
        
        