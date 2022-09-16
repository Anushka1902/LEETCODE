class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def find(ind,arr,target,ds):
            if target==0:
                ans.append(ds.copy())
                return
            for i in range(ind,len(arr)):
                if i>ind and arr[i]==arr[i-1]:
                    continue
                if arr[i]>target:
                    break
                ds.append(arr[i])
                find(i+1,arr,target-arr[i],ds)
                ds.pop()
        candidates.sort()
        find(0,candidates,target,[])
        return ans