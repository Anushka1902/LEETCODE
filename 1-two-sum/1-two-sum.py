class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        '''
        #brute-force approach
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        '''
        #optimal solution
        hashmap={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[nums[i]]=i
            