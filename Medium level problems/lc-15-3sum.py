#My initial solution to the problem
#This solution returns a single array multiple times if many elements present

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outer=list()
        sum_outer=0
        for i in range(0,len(nums)):
            sum_outer+=nums[i]
            sum_inner=0
            for j in range(i+1,len(nums)):
                sum_inner+=nums[j]
                for k in range(j+1,len(nums)):
                    sum_inner+=nums[k]
                    if nums[i]+nums[j]+nums[k]==0:
                        outer.append([nums[i],nums[j],nums[k]])
                sum_inner=nums[i]
        if outer!=None:
            return outer
        else:
            return []
