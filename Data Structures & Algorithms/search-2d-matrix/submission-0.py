class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        left,right=0,n*m-1
        
        while left<=right:
            mid=(left+right)//2
            # convert 2d to 1d
            row=mid//n
            col=mid%n
            value=matrix[row][col]

            if value==target:
                return True
            elif value<target:
                left=mid+1
            else:
                right=mid-1
        return False

        # m=len(matrix)
        # for i in range(len(matrix)):
        #     if matrix[i][0]<target and matrix[i][m-1]>target:
        #         return BS(matrix[i],target)
        