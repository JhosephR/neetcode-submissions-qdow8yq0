class Solution:
    def isPalindrome(self, s: str) -> bool:
        az = 'abcdefghilmnopqrstuvwxyz0123456789'
        l, r = 0, len(s)-1

        while l < r:
            while l < r and s[l].lower() not in az:
                l += 1
            while r > l and s[r].lower() not in az:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True