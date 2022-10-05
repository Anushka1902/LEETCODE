from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        pq=[]
        ans=[]
        heapify(pq)
        for i,val in hashmap.items():
            heappush(pq,(val,i))
            if len(pq)>k:
                heappop(pq)
        while pq:
            i,x=heappop(pq)
            ans.append(x)
        return ans
            
            