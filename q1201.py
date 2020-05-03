class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        # least common multiple 最小公倍數
        def lcm(x, y):
            return x * y // math.gcd(x, y)
        
        def count_ugly(mid, n):
            answer = mid // a + mid // b + mid // c
            answer -= mid // ab + mid // bc + mid // ca
            answer += mid // abc
            return answer >= n

        ab, bc, ca = lcm(a, b), lcm(b, c), lcm(c, a)
        abc = lcm(ab, c)
        l = 1
        r = 2 * 10 ** 9
        
        # binary search
        while l < r:
            mid = l + (r - l) // 2
            if count_ugly(mid, n):
                r = mid
            else:
                l = mid + 1
        return l
