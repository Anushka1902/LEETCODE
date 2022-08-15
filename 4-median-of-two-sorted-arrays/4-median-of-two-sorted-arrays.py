class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        n=nums1+nums2
        n.sort()
        b=len(n)
        if b%2==0:
            mid=b//2
            w=n[mid]
            x=n[mid-1]
            return((w+x)/2)
        else:
            ans=b//2
            return(n[ans])
        '''
        if len(nums2)<len(nums1):
            return self.findMedianSortedArrays(nums2,nums1)
        n1=len(nums1)
        n2=len(nums2)
        l=0
        r=n1
        while(l<=r):
            firstMid = l + (r-l)//2
            secondMid = (n1+ n2 + 1)//2 - firstMid
            leftFirst = -float('inf') if firstMid == 0 else nums1[firstMid-1]
            rightFirst = float('inf') if firstMid == n1 else nums1[firstMid]
            leftSecond = -float('inf') if secondMid == 0 else nums2[secondMid-1]
            rightSecond = float('inf') if secondMid == n2 else nums2[secondMid]
            if leftFirst <= rightSecond and leftSecond <= rightFirst:
                if ((n1+n2)%2==0):
                    return (max(leftFirst, leftSecond) + min(rightFirst, rightSecond))/2
                else:
                    return max(leftFirst, leftSecond)
            elif leftFirst > rightSecond:
                r = firstMid - 1
            else:
                l = firstMid + 1
        return -1