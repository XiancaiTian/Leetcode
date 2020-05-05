# LC 46
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

# LC 47
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:        
        def dfs(nums, d, n, used, curr, ans):
            if d == n:
                ans.append(curr[:])
                return
            
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                """
                因為要避免重複，所以要先查看同一個深度是否有過了一樣的數字
                已經用過了也沒關係，但是要按照順序使用，
                如果nums = [1,1,2], 則 第二個1一定要在第一個1已經出現在這條path裡，才可以使用
                """
                elif i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                curr.append(nums[i])
                dfs(nums, d+1, n, used, curr, ans)
                curr.pop()
                used[i] = False
        
        ans = []
        # 因為有重複，所以要先sort
        nums.sort()         
        dfs(nums, 0, len(nums), [False]*len(nums), [], ans)
        return ans
