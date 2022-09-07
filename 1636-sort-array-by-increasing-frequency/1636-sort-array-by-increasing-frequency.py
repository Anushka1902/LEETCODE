from heapq import *
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        seen = collections.Counter(nums) #Store in dictionary
    
        minHeap = [] 
        heapq.heapify(minHeap) #Make heap
    
        for key,value in seen.items():
    
            heapq.heappush(minHeap,(value,-key)) #heap push #Sort by value ascending and key descending
    
        output = []
    
        for i in range(len(seen)):
        
            pop = heapq.heappop(minHeap) #heap pop
        
            k = pop[1] * -1 #Make it back to positive
            val = pop[0]
        
            for i in range (val):
                output.append(k)
        return output