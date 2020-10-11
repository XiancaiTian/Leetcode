# non-traditional two pointer approach

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while left < right:
            sum_of_two = numbers[left]+numbers[right]             
            if sum_of_two == target:
                return [left+1, right+1]
            if sum_of_two >= target:
                right = right-1
            else:
                left = left + 1
        return [left+1, right+1]
