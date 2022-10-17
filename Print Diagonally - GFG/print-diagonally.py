#User function Template for python3

def downwardDigonal(N, A): 
    # code here
    ans=list()
    
    for i in range(N):
        col=i
        row=0
        while(col>=0):
            ans.append(A[row][col])
            row+=1
            col-=1
    for i in range(1,N):
        col=n-1
        row=i
        while(row<n):
            ans.append(A[row][col])
            row+=1
            col-=1
    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends