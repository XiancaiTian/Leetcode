# 半成品
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #return 0.0
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
        if m == 1:
            return nums1[0]
        
        ################################################
        # 套用花花左閉右開模板
        def findIndex():
            l, r, half_len = 0, m, (m + n + 1) // 2
            while l < r :
                i = (l + r) // 2
                j = half_len - i
                if i > 0 and A[i-1] >= B[j]:
                    # i is too big, must decrease it
                    r = i
                elif i < m and B[j-1] > A[i]:
                    # i is too small, must increase it
                    l = i + 1
            return l, half_len-l
            
        ################################################
        i, j = findIndex()
        print(i)

        # 邊界以左有k個數字，
        # 如果長度和為奇數，則邊界以左第一個的數字就是答案
        if i == 0: max_of_left = B[j-1]
        elif j == 0: max_of_left = A[i-1]
        else: max_of_left = max(A[i-1], B[j-1])

        if (m + n) % 2 == 1:
            return max_of_left

        if i == m: min_of_right = B[j]
        elif j == n: min_of_right = A[i]
        else: min_of_right = min(A[i], B[j])

        return (max_of_left + min_of_right) / 2.0
