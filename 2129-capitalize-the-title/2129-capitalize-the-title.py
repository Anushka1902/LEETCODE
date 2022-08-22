class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title.lower()
        li=title.split()
        mi=[]
        for i in li:
            if len(i)>2:
                i=i.capitalize()
                mi.append(i)
            else:
                i=i.lower()
                mi.append(i)
        ans=" ".join(mi)
        return ans
        