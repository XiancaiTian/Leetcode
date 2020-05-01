class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 利用ord(), 把character轉換成integer
        # a 對應 97
        # z 對應 122
        t = ord(target)
        
        # binary search 
        # 套用花花左閉右開upperbound模板 
        l, r = 0, len(letters)
        while l < r:
            mid = l + (r-l)//2
            if ord(letters[mid]) > t:
                r = mid
            else:
                l = mid + 1
        # while 結束後，l 會等於upperbound的index
        
        return letters[l] if l < len(letters) else letters[0]
