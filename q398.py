import collections
class Solution:
def __init__(self, nums: List[int]):
    self.mapping = collections.defaultdict(list)
    
    for i in range(len(nums)):
        self.mapping[nums[i]].append(i)
    

def pick(self, target: int) -> int:
    return choice(self.mapping[target])
