class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n >= 9:
            candidates = self.combine(9, k)
        else:
            candidates = self.combine(n, k)
        # copy the function of q77 and then filter the results
        return [sub for sub in candidates if sum(sub) == n] 
    
    # copy from q77
    def combine(self, n: int, k: int) -> List[List[int]]:
        # recursion soln inspired by
        # https://www.youtube.com/watch?v=qzdTZWW1X8A
        ans = []
        for i in range(1, n+1):
            if k-1 > 0:
                sub = [[i] + lst for lst in self.combine(i-1, k-1)]
            elif k == 1:
                sub = [[i]]
            else:
                sub = []
            ans.extend(sub)
        return ans
    
    
