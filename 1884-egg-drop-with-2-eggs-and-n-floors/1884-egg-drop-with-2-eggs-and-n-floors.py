class Solution:
    def twoEggDrop(self, n: int) -> int:
        for x in range(n+1):
            if x*(x+1)//2>=n:
                return x
            