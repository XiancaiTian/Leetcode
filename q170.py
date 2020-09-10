# dictionary approach

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums[number] += 1
            

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """          
            
        for i, v in self.nums.items():
            if (value - i) != i:
                if (value - i) in self.nums:
                    return True
            elif self.nums[i]>1:
                    return True
        return False
    
