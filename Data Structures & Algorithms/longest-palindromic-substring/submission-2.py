class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        max_length=0
        start=0

        def expand(left,right):
            nonlocal max_length,start

            while (left>=0 and right<len(s) and s[left]==s[right]):
                length=right-left+1

                if length>max_length:
                    max_length=length
                    start=left

                left-=1
                right+=1
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        return s[start:start+max_length]
























        # n=len(s)
        # longest=""

        # for i in range(n):
        #     for j in range(i,n):
        #         sub_str=s[i:j+1]

        #         if sub_str==sub_str[::-1] and len(sub_str)>len(longest):
        #             longest=sub_str
        # return longest
        