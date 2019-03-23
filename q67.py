class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(b) > len(a):
            a, b = b, a
            # a is always longer
        carry = 0
        sum_str = ''
        for idx in range(len(a)-1, -1, -1):
            loc_b = idx - (len(a) - len(b))
            if loc_b>=0:
                val = int(a[idx]) + int(b[loc_b]) + carry
            else:
                val = int(a[idx]) + carry
            if val > 1:
                carry = 1
                sum_str = str(val-2) + sum_str
            else:
                carry = 0
                sum_str = str(val) + sum_str
        if carry:
            sum_str = '1' + sum_str
        return sum_str
