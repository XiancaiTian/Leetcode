class Solution:
    # 套用huahua的permutation template
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums, d, n, used, curr, ans):
            if d == n:
                ans.append(curr[:])
                return
            
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                curr.append(nums[i])
                dfs(nums, d+1, n, used, curr, ans)
                curr.pop()
                used[i] = False
        
        ans = []
        dfs(nums, 0, len(nums), [False]*len(nums), [], ans)
        return ans
