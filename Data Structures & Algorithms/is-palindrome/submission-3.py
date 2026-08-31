class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=list(s)
        a="abcdefghijklmnopqrstuvwxyz"
        n="0123456789"
        ans=""
        for i in s:
            if i in a or i in n:
                ans+=i
        return ans==ans[::-1]