class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=min_product=result=nums[0]

        n=len(nums)

        for i in range(1,n):
            if nums[i]<0:
                max_product,min_product=min_product,max_product
            max_product=max(max_product*nums[i],nums[i])
            min_product=min(min_product*nums[i],nums[i])

            result =max(result,max_product)
        return result


















        # max_product=nums[0]
        # n=len(nums)

        # for i in range(n):
        #     product=1
        #     for j in range(i,n):
        #         product*=nums[j]
        #         max_product=max(max_product,product)
        # return max_product
        