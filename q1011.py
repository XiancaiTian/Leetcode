class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def canShip(weights, mid, D):
            total, count = 0, 1
            for n in weights:
                if total + n <= mid:
                    total +=n
                else:
                    count +=1
                    total = n
                if count >D:
                    return False
            return True
        
        # binary search
        l , r = max(weights), sum(weights)
        while l < r:
            mid = l + (r-l) //2
            if canShip(weights, mid, D):
                r = mid
            else:
                l = mid + 1
        return l
