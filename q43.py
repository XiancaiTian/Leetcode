class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        L1, L2 = len(num1), len(num2)
        value = 0
        for i1 in range(L1-1, -1, -1):
            reverse_i1 = L1-i1-1 # id from the back
            for i2, v2 in enumerate(num2):
                reverse_i2 = L2-i2-1  # id from the back
                value += int(num1[i1])*int(v2)*(10**reverse_i2)*(10**reverse_i1)
        return str(value)
