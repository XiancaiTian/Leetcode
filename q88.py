class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2
        elif n == 0:
            nums1
        else:
            j1, j2 = m-1, n-1
            for i in range(m+n-1,-1,-1):
                # want to update nums1[i]
                if nums1[j1]>=nums2[j2]:
                    nums1[i]=nums1[j1]
                    j1-=1
                else:
                    nums1[i]=nums2[j2]
                    j2-=1
                if j1 <0:
                    nums1[:i] = nums2[:j2+1]
                    break
                elif j2<0:
                    nums1[:i] = nums1[:j1+1]
                    break
        # Note: what if input is empty list.... 
