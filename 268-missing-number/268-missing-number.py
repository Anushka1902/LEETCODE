class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        '''
        '''
        n=len(nums)
        totalsum=((n)*(n+1))//2
        arr_sum=sum(nums)
        return totalsum-arr_sum
        '''
        all_no_xor = 0
        for i in range(len(nums)+1):
            all_no_xor ^= i
            
        missing_xor = 0
        for num in nums:
            missing_xor ^= num
            
        return all_no_xor ^ missing_xor