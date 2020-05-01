class Solution:   
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, len(nums)
        
        # 仿照leetcode 278, 自己定義一個isBadVersion
        # 當single number 出現之後
        # isBadVersion就會return False
        # 以 [1,1,2,3,3]為例
        # 也就是 [F,F,F,T,T]
        def isBadVersion(index):
            if index == 0:
                return False
            if index%2 == 1:
                return nums[index] != nums[index-1]
            if index%2 == 0:
                return nums[index] == nums[index-1]
        
        # 進行Binary search, 找到第一個寫錯的數字
        # 正常來說，每個數字都要寫兩次
        # 所以如果有個地方該寫第二次卻沒有，就是寫錯了
        while l < r:
            mid = l + (r-l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid +1
        
        # 往前推一位，就是single的數字
        return nums[l-1]
