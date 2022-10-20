class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones=[]
        length=len(nums)
        for i in range(length):
            if nums[i]==1:
                ones.append(i)
        print(ones)
        n=len(ones)
        presum=[0]*(n+1)
        for i in range(n):
            presum[i+1]=presum[i]+ones[i]
        res=inf
        if k%2==1:
            #odd window
            radius=(k-1)//2
            for  i in range(radius,n-radius):
                right = presum[i+radius+1]-presum[i+1]
                left = presum[i]-presum[i-radius]
                res = min(res, right-left)
            return res-radius*(radius+1)
        else:
            radius=(k-2)//2
            for i in range(radius,n-radius-1):
                right=presum[i+radius+2]-presum[i+1]
                left=presum[i]-presum[i-radius]
                res=min(res,right-left-ones[i])
            return res-radius*(radius+1)-(radius+1)
            
        '''    
        left=0
        right=k
        window=[]
        while right<length-k:
            window.append(ones[left:right])
            left+=1
            right+=1
        print(window)
        ans=999999
        for win in window:
            suma=0
            l=0
            r=len(win)
            middle=(l+r)//2
            while l<middle and r>middle:
                suma+=(middle-l)+(right-middle)
            ans=min(ans,suma)
        print(ans)
        '''   
            