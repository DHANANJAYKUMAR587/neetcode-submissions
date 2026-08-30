class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=sorted(d.items(), key=lambda x: x[1])
        ans=[]
        for key,val in a:
            ans.append(key)
        return ans[-k:]