#User function Template for python3
from collections import defaultdict
class Solution:
	def characterReplacement(self, s, k):
		# Code here
		c=defaultdict(int)
		res,maxcount=0,0
		for index,value in enumerate(s):
		    c[value]+=1
		    maxcount=max(maxcount,c[value])
		    if res-maxcount>=k:
		        c[s[index-res]]-=1
		    else:
		        res+=1
		return res
		'''
		def findlen(A,k,ch):
		    maxlen=0
		    cont=0
		    l=0
		    r=0
		    n=len(A)
		    while r<n:
		        if A[r]!=ch:
		            cont+=1
		        while cont>k:
		            if A[l]!=ch:
		                cont-=1
		            l+=1
		        maxlen=max(maxlen,r-l+1)
		        r+=1
		    return maxlen
		maxlength=1
		for i in range(26):
		    maxlength=max(maxlength,findlen(s,k,chr(i+ord('A'))))
		    #maxlength=max(maxlength,findlen(s,n,k,chr(i+ord('a'))))
		return maxlength
		'''
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		k = int(input())
		ob = Solution()
		ans = ob.characterReplacement(s, k)
		print(ans)

# } Driver Code Ends