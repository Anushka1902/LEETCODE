class Solution:
    def isValid(self, weights, proposedCapacity, days):
        capacity = 0
        daysTaken = 0
        for weight in weights:
            if weight > proposedCapacity:
                return False
            if capacity + weight <= proposedCapacity:
                capacity += weight
            else:
                capacity = weight
                daysTaken += 1
        daysTaken += 1
            
        return daysTaken <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        minCapacity = end
        while start < end:
            mid = start + ((end-start)//2)
            if self.isValid(weights, mid, days):
                # Potential answer found.
                minCapacity = mid
                end = mid
            else:
                # Need to increase the capacity!
                start = mid + 1
        return minCapacity

    