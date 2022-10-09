class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid,x,y,r,c):
            if x<0 or x>=r or y<0 or y>=c or grid[x][y]!='1':
                return 
            grid[x][y]='2'
            dfs(grid,x+1,y,r,c)
            dfs(grid,x-1,y,r,c)
            dfs(grid,x,y+1,r,c)
            dfs(grid,x,y-1,r,c)
        nr=len(grid)
        nc=len(grid[0])
        numberofislans=0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j]=='1':
                    dfs(grid,i,j,nr,nc)
                    numberofislans+=1
        return numberofislans