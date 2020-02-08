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
