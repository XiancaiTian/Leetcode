class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # cut the string by last letter from M, D, C, L, V, X
        # if other letters occur inside, means minus those...        
        romans = [('M',1000, 2),('D',500, 2), ('C',100, 4), 
                  ('L', 50, 4), ('X', 10, 6), ('V', 5, 6), ('I', 1, 'stop')]
        number = 0
        for (letter, value, subtract) in romans:
            loc = s.rfind(letter)
            if letter == 'I':
                add = s[:loc+1].count(letter)*value
                number += add
                return number
            elif loc >-1:
                minus = (s[:loc+1].count(romans[subtract][0]))*romans[subtract][1]
                add = s[:loc+1].count(letter)*value
                number = number + add - minus
                print(number)
                if loc+1<len(s):
                    s=s[loc+1:]
                else:
                    break
        return number
