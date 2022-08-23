class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.strip().split(' ')
        #print(arr)
        res=''
        for i in range(len(arr)-1,-1,-1):
            if arr[i]!="":
                res+=' '+arr[i]
        return res.strip()