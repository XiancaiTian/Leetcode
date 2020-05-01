class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #return 0.0
        n1, n2 = len(nums1), len(nums2)
        if n2 < n1:
            nums1, nums2, n1, n2 = nums2, nums1, n2, n1        
        
        ################################################
        # 套用花花左閉右開模板                  # 套用花花左閉右閉模板
        def findIndex():
            # 在比較短的nums上面移動index
            # 直到卡住不動的時候 (22和24的條件都不符合的時候) 
            # For example, nums1 = [0,0] nums2 = [0,0]
            # 或是離開while的時候
            # For example, nums1 = [1,3], nums2 = [2]
            l, r, half_len = 0, n1, (n1 + n2 + 1) // 2
            while l < r :                      # while l <= r
                i = (l + r) // 2
                j = half_len - i
                if i > 0 and nums1[i-1] > nums2[j]:
                    r = i                      # r = i + 1
                elif i < n1 and nums2[j-1] > nums1[i]:
                    l = i + 1
                else:
                    return i, half_len-i
            return l, half_len-l
            
        ################################################
        i, j = findIndex()
        # 邊界以左有k個數字，
        # 如果長度和為奇數，則要找邊界以左最大的數字max_of_left
        if i == 0: max_of_left = nums2[j-1]
        elif j == 0: max_of_left = nums1[i-1]
        else: max_of_left = max(nums1[i-1], nums2[j-1])

        # 如果nums最長度是奇數，就直接回傳max_of_left
        if (n1 + n2) % 2 == 1:
            return max_of_left
        # 如果nums最長度是偶數，要找到max_of_left以及右邊最小的數min_of_right
        # 取平均數作為答案
        if i == n1: min_of_right = nums2[j]
        elif j == n2: min_of_right = nums1[i]
        else: min_of_right = min(nums1[i], nums2[j])
        return (max_of_left + min_of_right) / 2.0
