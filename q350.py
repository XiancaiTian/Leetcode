class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # O(n2logn2)
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        # assume nums1 is shorter
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        p1, p2 = 0, 0
        l1, l2 = len(nums1), len(nums2)
        ans = []
        # O(n1)
        while p1 < l1 and p2 < l2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                ans.append(nums1[p1])
                p1 += 1
                p2 += 1
                
        return ans
