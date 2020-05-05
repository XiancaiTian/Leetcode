class Solution:
    """
    "a1b2" can be simplified as [ab, aB, Ab, AB] plus the unchanged number 1 2 
    雖然題目叫做permutation, 其實要套用combination template
    Edge case: input可能會有大寫字母
    """
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(S, d, n, s, curr, ans):
            if d == n:
                ans.append(''.join(curr[:]))
                return
           
            for i in range(s, len(S)):
                word_candidates = [S[d]] if S[d].isdigit() else [S[d].lower(), S[d].upper()]
                for word in word_candidates:
                    curr.append(word)
                    dfs(S, d+1, n, i+1, curr, ans)
                    curr.pop()
        
        ans = []
        dfs(S, 0, len(S), 0, [], ans)
        return ans
