class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        
        # filtering every non number, minus, plus...
        add = str[0]
        for s in str[1:]:
            if not s.isdigit():
                add+=' '
            else:
                add+=s
        str = add
        
        if ' ' in str:
            str = str.split(' ')[0]

        try:
            ans = int(str)
        except ValueError:
            ans = 0
        except OverflowError:
            ans == 0
        if ans > 2147483647:
            return 2147483647
        elif ans< -2147483648:
            return -2147483648
        else:
            return ans
