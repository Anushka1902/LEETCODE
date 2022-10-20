#User function Template for python3
class Solution:
    def reverseSpiral(self, m, n, matrix):
        ans = []
     
        seen = [[0 for i in range(n)] for j in range(m)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        x = 0
        y = 0
        di = 0
     
        # Iterate from 0 to R * C - 1
        for i in range(m * n):
            ans.append(matrix[x][y])
            seen[x][y] = True
            cr = x + dr[di]
            cc = y + dc[di]
     
            if (0 <= cr and cr < m and 0 <= cc and cc < n and not(seen[cr][cc])):
                x = cr
                y = cc
            else:
                di = (di + 1) % 4
                x += dr[di]
                y += dc[di]
        return ans[::-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C=[int(x) for x in input().split()]
        a=[[0]*C for c in range(R)]
        arr=input().split()
        for i in range(R*C):
            a[i//C][i%C]=int(arr[i])
            
        ob=Solution()
        ans=ob.reverseSpiral(R,C,a)
        for i in range(len(ans)):
            print(ans[i],end=" ")
            
        print()
# } Driver Code Ends