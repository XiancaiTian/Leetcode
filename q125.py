class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(" ","").lower()
        s = ''.join([char for char in s if char.isalpha() == True or char.isnumeric() == True])
        q, r = divmod(len(s), 2)
        if q==0:
            return True
        else:
            return s[:q][::-1] == s[-q:]
