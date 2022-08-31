class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a,b):
            if a==0:
                return b
            return gcd(b%a,a)
        def lcm(a,b):
            return (a*b)//gcd(a,b)
        stack=[nums[0]]
        for i in nums[1:]:
            y=i
            while len(stack)>0 and gcd(y,stack[-1])>1:
                x=stack.pop()
                y=lcm(x,y)
            stack.append(y)
        return stack
            