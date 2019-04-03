class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s != '':
            s = list(s)
            vowels = 'AOEIUaoeiu'
            i = 0
            j = len(s) - 1
            while j>i:
                if s[i] not in vowels:
                    i += 1
                if s[j] not in vowels:
                    j -= 1
                if s[i] in vowels and s[j] in vowels:
                    s[i],s[j] = s[j],s[i]
                    i += 1
                    j -= 1
        return ''.join(s)
