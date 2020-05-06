class Solution:
    # permutation plus pruning
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(nums, d, n, used, curr, ans):
            if d == n:
                ans.append(''.join(curr))
                return
            
            for i in range(0, len(nums)):
                if used[i]:
                    continue

                elif i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # Prune 關鍵：一定要有開才可以有關
                elif nums[i]== ')' and curr.count('(') <= curr.count(')'):
                    continue
                
                used[i] = True
                curr.append(nums[i])
                dfs(nums, d+1, n, used, curr, ans)
                curr.pop()
                used[i] = False
        
        ans = []
        nums = '('*n + ')'*n            
        dfs(nums, 0, len(nums), [False]*len(nums), [], ans)
        return ans
