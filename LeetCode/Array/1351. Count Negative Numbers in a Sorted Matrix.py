class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        n=len(grid)
        m=len(grid[0])-1
        for i in range(0,n):
            for j in range(m,-1,-1):
                if grid[i][j]<0:
                    count+=1
                else:
                    break
        return count

        
