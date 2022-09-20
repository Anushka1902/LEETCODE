class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        check=set()
        queue=[start]
        while len(queue):
            curr=queue.pop(0)
            if arr[curr]==0:
                return True
            for x in (curr+arr[curr],curr-arr[curr]):
                if 0<=x<len(arr) and x not in check:
                    queue.append(x)
                    check.add(x)
        return False