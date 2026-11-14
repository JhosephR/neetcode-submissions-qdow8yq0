class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s) - 1
        lf = rf = False

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            if not lf:
                if rf:
                    r += 1
                lf = True
                l += 1
            elif not rf:
                if lf:
                    l -= 1
                rf = True
                r -= 1
            else:
                return False
        return True