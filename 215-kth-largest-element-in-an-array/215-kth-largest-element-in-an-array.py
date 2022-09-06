from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        heapq.heapify(nums)
        target=len(nums)-k
        for i in range(target):
            heapq.heappop(nums)
        return heapq.heappop(nums)
        '''
        '''
        return sorted(nums,reverse=True)[k-1]
        '''
        minl=[]
        heapify(minl)
        for i in nums:
            heappush(minl,i)
            if len(minl)>k:
                heappop(minl)
        return minl[0]
        