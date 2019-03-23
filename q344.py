class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for idx in range(len(s)/2):
            store = s[idx]
            s[idx] = s[(-1)*(idx+1)]
            s[(-1)*(idx+1)] = store
