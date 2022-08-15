class Solution:
    def mySqrt(self, x: int) -> int:
        #binary-Search
        s=0
        e=x
        while(s<=e):
            mid=s+(e-s)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                ans=mid
                s=mid+1
            else:
                e=mid-1
        return ans
        #linear Search
        #SC-O(1)
        #TC-O(rootx)
        '''
        y=0
        while(y*y<=x):
            y+=1
        return y-1
        '''
    