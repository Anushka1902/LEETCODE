class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        arr=nums
        li=[1]*n
        cnt=[1]*n
        for i in range(n):
            s1=li[i]
            s=1
            for j in range(0,i):
                if arr[i]>arr[j]:
                    if s1<li[j]+1:
                        s1=max(s1,li[j]+1)
                        s=cnt[j]
                    elif s1==li[j]+1:
                        s+=cnt[j]
            cnt[i]=s
            li[i]=s1
        maximum=max(li)
        ans=0
        for i in range(n):
            if maximum==li[i]:
                ans+=cnt[i]
        return ans
        