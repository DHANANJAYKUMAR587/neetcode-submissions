class Solution:
    def twoSum(self,f,ans,nums):
        i=f+1
        j=len(nums)-1
        while i<j:
            total=nums[f]+nums[i]+nums[j]
            if total>0:
                j-=1
            elif total<0:
                i+=1
            else:
                ans.append([nums[f],nums[i],nums[j]])
                i+=1
                j-=1
                while i<j and nums[i]==nums[i-1]:
                    i+=1
                while i<j and nums[j]==nums[j+1]:
                    j-=1
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]
        for f in range(len(nums)):
            if nums[f]>0:
                continue
            elif f==0 or nums[f]!=nums[f-1]:
                self.twoSum(f,ans,nums)
        return ans