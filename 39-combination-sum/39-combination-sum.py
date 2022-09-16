class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def find(ind,arr,target,ds):
            if ind==len(arr):
                if target==0:
                    ans.append(ds.copy())
                return
            if arr[ind]<=target:
                ds.append(arr[ind])
                find(ind,arr,target-arr[ind],ds)
                ds.pop()
            find(ind+1,arr,target,ds)
        find(0,candidates,target,[])
        return ans