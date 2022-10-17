class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr=[0]*26
        for i in sentence:
            index=ord(i)-97
            arr[index]+=1
        num=arr.count(0)
        if num>0:
            return False
        return True