class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        lis=[1]*n
        cnt=[1]*n
        for i in range(n):
            maxi=lis[i]
            count=1
            for j in range(0,i):
                if nums[i]>nums[j]:
                    if maxi<lis[j]+1:
                        maxi=max(maxi,lis[j]+1)
                        count=cnt[j]
                    elif maxi==lis[j]+1:
                        count+=cnt[j]
            cnt[i]=count
            lis[i]=maxi
        maxs=max(lis)
        ans=0
        for i in range(n):
            if maxs==lis[i]:
                ans+=cnt[i]
        return ans