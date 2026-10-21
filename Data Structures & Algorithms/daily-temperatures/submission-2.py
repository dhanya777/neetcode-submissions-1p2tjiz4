class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n=len(temperatures)
        res=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                pre_index=stack.pop()
                res[pre_index]=i-pre_index
            else:
                stack.append(i)
        return res
            # for j in range(i,n):
            #     if temperatures[j]>temperatures[i]:
            #         res[i]=j-i
            #         break
                
        # return res
        