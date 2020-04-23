class Solution:
    def __init__(self, nums):
        self.array = nums
        # need to clone the nums, otherwise it will be affected by self.array
        self.original = list(nums)

    def reset(self):
        return self.original
    
    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
