class Solution:
    def maxDepth(self, s: str) -> int:
        maxc=0
        count=0
        stack=[]
        for i in s:
            if i =='(':
                stack.append(i)
            elif i==')':
                stack.pop()
            else:
                continue
            maxc=max(maxc,len(stack))
        return maxc