class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        heap = []
        if(len(arr) == None): return res

        for i in range(len(arr)):
            diff = abs(x - arr[i])
            heapq.heappush(heap, [diff, arr[i]])

        for _ in range(k):
            diff, num = heapq.heappop(heap)
            res.append(num)
            
        res.sort()    
        return res