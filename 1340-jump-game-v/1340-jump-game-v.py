class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        arr2=[(num,index) for index,num in enumerate(arr)]
        arr2.sort()
        n=len(arr)
        dp=[0]*n
        for _,i in arr2:
            maxx=1
            #leftside
            left=max(-1,i-d-1)
            for j in range(i-1,left,-1):
                if arr[j]>=arr[i]:
                    break
                maxx=max(dp[j]+1,maxx)
            #rightside
            right=min(len(arr),i+d+1)
            for j in range(i+1,right):
                if arr[j]>=arr[i]:
                    break
                maxx=max(dp[j]+1,maxx)
            dp[i]=maxx
        return max(dp)