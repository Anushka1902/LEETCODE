#User function Template for python3

class Solution:
    def fillingBucket(self, N):
        # code here
        dp = [0]*(N+1)
        dp[0] = 1
        dp[1] = 1
        
        mod = 100000000
        
        for i in range(2, N+1):
            dp[i] = (dp[i-1]+dp[i-2])%mod
            
        return dp[N]%mod

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.fillingBucket(N))
# } Driver Code Ends