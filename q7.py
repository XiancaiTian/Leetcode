class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2147483648 or x < -2147483648:
            return 0
        s = list(str(x))
        if s[0] =='-':
            s = s[1:]
            multiply = (-1)
        else:  
            multiply = 1
        last = len(s)

        for i, char in enumerate(s):
            if i >= last/2:
                break
            elif char!='-':
                store = s[last-i-1]
                s[last-i-1] = s[i]
                s[i] = store
        ans = int(''.join(s))*multiply
        if ans > 2147483648 or ans < -2147483648:
            return 0
        else:
            return ans
            
