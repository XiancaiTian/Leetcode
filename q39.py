# LC 39
class Solution(object):
    # 套用 Huahua combination template 並修改
    def combinationSum(self, candidates, target):
        # s: 從第幾個數開始取，取了一個數就不可以取前面的數了
        def dfs(candidates, target, s, curr, ans):
            if target == 0: 
                # 記得要deepcopy curr
                ans.append(curr[:])
                return
            
            for i in range(s, len(candidates)):
                # 剪枝的動作
                if candidates[i] > target: 
                    return
                
                curr.append(candidates[i])
                # 原本的template 會讓下一步的s = i+1
                # 因為這題可以使用重複的數字，所以寫作i
                dfs(candidates, target - candidates[i], i, curr, ans)
                curr.pop()
        
        ans = []
        # 要先sort過，避免走到重複的路
        candidates.sort()
        # dfs開始: http://zxi.mytechroad.com/blog/searching/leetcode-39-combination-sum/
        dfs(candidates, target, 0, [], ans);       
        return ans
 
# LC 40
class Solution:
    # 套用 Huahua combination template 並修改成 leetcode 39, 然後再改成 leetcode 40
    # 39題的input不會有重複的數，但是40有，如果照抄的話就會有重複的答案
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # s: 從第幾個數開始取，取了一個數就不可以取前面的數了

        def dfs(candidates, target, s, curr, ans):
            if target == 0: 
                # 記得要deepcopy curr
                ans.append(curr[:])
                return
            

            for i in range(s, len(candidates)):
                # 剪枝的動作
                if candidates[i] > target: 
                    return
                
                # 和LEETCODE 39不一樣的地方1
                if i > s and candidates[i] == candidates[i-1]:
                    # avoid repetition
                    continue
                
                curr.append(candidates[i])
                
                # 和LEETCODE 39不一樣的地方2, 本來是i, 代表input的數字可以重複使用多次，
                # 這裡是i+1，不允許使用重複的，除非input裡面本來就有兩個
                dfs(candidates, target - candidates[i], i+1, curr, ans)
                curr.pop()
        ans = []
        candidates.sort()
        dfs(candidates, target, 0, [], ans);       
        return ans

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 延續leetcode 39, 但是固定candidates，要求深度固定為 k, target為n
        candidates = [i + 1 for i in range(9)]
    
        # s: 從第幾個數開始取，取了一個數就不可以取前面的數了
        # 續記錄深度
        def dfs(candidates, target, d, k, s, curr, ans):
            if target == 0 and d == k : 
                ans.append(curr[:])
                return
            
            for i in range(s, len(candidates)):
                # 剪枝的動作
                if candidates[i] > target: 
                    return
                
                curr.append(candidates[i])
                # 和LEETCODE 39不一樣的地方2, 本來是i, 代表input的數字可以重複使用多次，
                # 這裡是i+1，不允許使用重複的，除非input裡面本來就有兩個
                dfs(candidates, target - candidates[i], d+1, k, i+1, curr, ans)
                curr.pop()
        ans = []
        candidates.sort()
        dfs(candidates, n, 0, k, 0, [], ans);       
        return ans
 





# source https://leetcode.com/problems/combination-sum-ii/discuss/497792/Python-sol.-by-DFS-and-pruning.-93%2B-With-explanation
### LEETCODE 39
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # preprocessing, sort candidates in ascending order
        candidates.sort()

        # record of minimum element in candidates
        mini = candidates[0]

        # record the valid combination
        result = []

        def combination_find(target, start, end, path):

            if target == 0:
                # path sum equals to target, find one valid combination
                result.append(path)
				return

            for i in range(start, end + 1):
                cur = candidates[i]
                
                if cur > target:
                    # pruning:
                    # current minimum element is larger that target
                    # impossible to make combination
                    break

                remaining = target - cur

                if remaining and remaining < mini: 
                    # remainder is smaller than smallest number in candidates
                    continue
            
                # DFS search:
                combination_find(remaining, i, end, path + [cur])

        # DFS search
        combination_find(target, 0, len(candidates) - 1, [])
        return result

### LEETCODE 40
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # keep candidates in ascending order
        candidates.sort()
        
        # record of valid combination
        result = []
        
        def combination_find( target, start, end, path):
            
             
            if target == 0:
                # combination sum meets target
                # update current valid combination
                result.append( path )
                return 
            
            for i in range(start, end+1):     
                           
                if i > start and candidates[i] == candidates[i-1]:
                    # avoid repetition
                    continue
                    
                current = candidates[i]
                
                if current > target:
                    # pruning:
                    # current minimal element is larger than target
                    # impossible to find valid combination
                    break
                
                # update target in next round as remaining
                remaining = target - current
                
                # DFS search, update start index as i+1 and move forward
                combination_find(remaining, i+1, end, path + [ current ] )
        
        # DFS search
        combination_find( target, 0, len(candidates)-1, [] )
        return result
