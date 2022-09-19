from math import gcd
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res=0
        n=len(nums)
        di=defaultdict(int)
        for i in range(n):
            gcd1=gcd(nums[i],k)
            gcd2=k//gcd1
            if gcd2==1:
                res+=i
            else:
                for x,y in di.items():
                    if x%gcd2==0:
                        res+=y
            di[gcd1]+=1
        return res