class Solution:
    # 套用 LC 47 permutation with duplicates, 然後進行剪枝
    def numSquarefulPerms(self, A: List[int]) -> int:
    
        def isSquareful(x, y):
            return int((x+y)**0.5) ** 2 == x+y
        
        def dfs(nums, d, n, used, curr, ans):
            if d == n:
                ans.append(True)
                return
            
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                    
                # delete repetitions
                elif i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                    
                # Pruning: 檢查這條path是否符合isSquareful
                elif curr and not isSquareful(curr[-1], nums[i]):
                    continue
                    
                used[i] = True
                curr.append(nums[i])
                dfs(nums, d+1, n, used, curr, ans)
                curr.pop()
                used[i] = False
        
        ans = []
        # 因為有重複，所以要先sort
        A.sort()
        dfs(A, 0, len(A), [False]*len(A), [], ans)
        return sum(ans)
