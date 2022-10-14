#User function Template for python3

from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        n, m = len(grid), len(grid[0])
        
        Q = [source]
        grid[source[0]][source[1]] = 0
        dist = 0
        while Q:
            new_Q = []
            for x, y in Q:
                if [x,y] == destination:
                    return dist
                for dx, dy in [[0,1],[0,-1],[-1,0],[1,0]]:
                    nx, ny = x+ dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        new_Q.append([nx, ny])
            dist += 1
            Q = new_Q
        return -1
                        
                        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends