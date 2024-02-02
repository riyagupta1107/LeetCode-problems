#Two Sum problem
#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            sum=nums[i]
            for j in range(i+1,len(nums)):
                sum+=nums[j]
                if sum==target:
                    return i,j
                else:
                    sum=nums[i]
