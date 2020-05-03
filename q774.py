class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        def possible(D):
            # 如果每D的距離就要加一個station
            # 請問會加幾個station呢
            # 如果算出來的station總數>K, return False
            # 如果算出來的station總數<=K, return True
            return sum(int((stations[i+1] - stations[i]) / D)
                       for i in range(len(stations) - 1)) <= K
        """
        想要用binary search 找出D
         但是D不會是整數，所以要做變化....
        """
        # stations[i] will be an integer in range [0, 10^8]
        lo, hi = 0, 10**8 
        # Answers within 10^-6 of the true value will be accepted as correct.
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo
