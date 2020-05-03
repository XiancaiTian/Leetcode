class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # 用((n-1)//mid +1)算出吃掉那個pile需要的時間
        # 如果會超時，就return False
        def canFinish(piles, mid, H):
            count = 0
            for n in piles:
                count += ((n-1)//mid +1)
                if count > H:
                    return False
            return True
        
        """for debugging purpose
        for i in range(l,r):
            print(i, canFinish(piles, i, H))
        """
        
        # 套用binary search
        l, r = 1, max(piles)
        while l<r:
            mid = l + (r - l)//2
            if canFinish(piles,mid,H):
                r = mid
            else:
                l = mid + 1
        return l
