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
