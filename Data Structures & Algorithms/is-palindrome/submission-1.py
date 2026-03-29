class Solution:
    def isPalindrome(self, s: str) -> bool:
        az = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = (''.join(s.split(' '))).lower()
        ans, rev = '', ''
        for c in s:
            if c in az:
                ans += c
        for i in range(len(ans)-1, -1, -1):
            rev += ans[i]
        return ans == rev