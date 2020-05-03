# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def binaryGuess(mid):
            return guess(mid) <= 0
        """
        let's say we have input array [1,2,3,4,5,6], pick = 4
        when we loop throught each of the elements, 
        we want binaryGuess return [F, F, F, T, T, T]
        """
        # binary search
        l, r = 1, n  
        while l < r:
            mid = l + (r-l)//2
            if binaryGuess(mid):
                r = mid
            else:
                l = mid + 1
        return l
