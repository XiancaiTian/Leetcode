class Solution:
    """
    input:     [1,         2,          3,          1              ]
    direction: [up (1=>2), up (2=>3) , down (3=>1), down (1=>-Inf)]
    """
    def findPeakElement(self, nums: List[int]) -> int:
        nums = nums + [-float("Inf")]
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            # 只要看到下降的趨勢 代表你要找的點(peak)會在左邊
            if nums[mid]>=nums[mid+1]:
                r = mid
            # 只要看到上升的趨勢 代表你要找的點(peak)會在左邊
            else:
                l = mid + 1
        return l
    """
    Note: 因為這提不會有重複的elements,
    用lower bound or upperbound模板都可以；
    可以 if nums[mid]>=nums[mid+1]，也可以是 if nums[mid]>nums[mid+1]
    但是要小心以mid+1為index之後，不然可能會超過Array的長度
    因此 在第三行的時候 我多加了 nums = nums + [-float("Inf")]
    """
