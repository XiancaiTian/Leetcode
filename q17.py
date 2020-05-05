class Solution:
    """
    和經典的combination不同，這裡每一層的candidate都不一樣
    """ 
    def letterCombinations(self, digits: str) -> List[str]:
        d = len(digits)
        k = len(digits)
        mapping = ['abc','def','ghi','jkl','mno','pqrs','tuv','wzyx']
        
        """
        和經典的combination dfs()不同，這裡省略了nums, s
        """
        def dfs(d, k, curr, ans):
            if d == k:
                ans.append(''.join(curr[:]))
                return
            candiates_this_depth = mapping[int(digits[d])-2]
            for word in candiates_this_depth:
                curr.append(word)
                dfs(d+1, k, curr, ans)
                curr.pop()
                
        # edge case
        if not digits: 
            return []
        
        ans = []
        dfs(0, k, [], ans)
        return ans
