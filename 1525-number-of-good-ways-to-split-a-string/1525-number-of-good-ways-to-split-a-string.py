class Solution:
    def numSplits(self, s: str) -> int:
            riht=Counter(s)
            left=set()
            swa=0
            for i in s:
                left.add(i)
                riht[i]-=1
                if not riht[i]:
                    del riht[i]
                if len(left)==len(riht):
                    swa+=1
            return swa