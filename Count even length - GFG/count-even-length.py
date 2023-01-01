#User function Template for python3
import math
class Solution:
	def compute_value(self, n):
		# Code here
        t = math.factorial(n)
        return (math.factorial(2*n) // t // t) % (10**9+7)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.compute_value(n)
		print(ans)
# } Driver Code Ends