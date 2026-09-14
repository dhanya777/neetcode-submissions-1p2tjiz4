class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]

        for i in range(len(intervals)):
            start,end=intervals[i]

            if end < newInterval[0]:
                result.append(intervals[i])
            
            elif start > newInterval[1] :
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            else:
                newInterval[0]=min(newInterval[0],start)
                newInterval[1]=max(newInterval[1],end)

        result.append(newInterval)
        
        return result


        