# My solution
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

    
"""
Author: Huahua
Running time: 92 ms
"""
class Solution:
  def letterCasePermutation(self, S):
    ans = []
 
    def dfs(S, i, n):
      if i == n:
        ans.append(''.join(S))
        return
    
      # 無論是字母或數字，都讓深度+1, 進到下一個dfs()
      dfs(S, i + 1, n)      
      if not S[i].isalpha(): return
      # 如果是字母的話，要做大小寫轉換，然後多一個dfs()
      S[i] = chr(ord(S[i]) ^ (1<<5))
      dfs(S, i + 1, n)
      # 大小寫轉換用完了，把他復原
      S[i] = chr(ord(S[i]) ^ (1<<5))
    
    dfs(list(S), 0, len(S))
    return ans
