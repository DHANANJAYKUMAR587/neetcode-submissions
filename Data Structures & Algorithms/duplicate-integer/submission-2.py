class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if max(d.values())>1:
            return True
        return False