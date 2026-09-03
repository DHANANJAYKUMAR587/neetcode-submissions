class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=[]
        total=0
        for i in range(len(s)):
            ans.append(ord(s[i]))
        for i in range(len(ans)-1):
            total+=abs(ans[i+1]-ans[i])
        return total