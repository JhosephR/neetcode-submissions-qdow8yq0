class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        left = right = False

        while l < r:
            if s[l] != s[r]:
                if not left:
                    if right:
                        r += 1
                    left = True
                    l += 1
                elif not right:
                    if left:
                        l -= 1
                    right = True
                    r -= 1
                else:
                    return False
            else:
                l += 1
                r -= 1
        return True