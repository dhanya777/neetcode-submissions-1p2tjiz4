class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result=[]
        count=0
        

        for start,end in intervals:
            
            if not result or result[-1][1]<=start:
                result.append([start,end])
            else:
                count+=1
                if end<result[-1][1]:
                    result.append([start,end])
        return count
        