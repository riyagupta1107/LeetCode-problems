# Algorithm of complexity O(n)
class Solution:
    def findMin(self, nums):
        val = False
        if len(nums) == 0:
            return -1
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                val = True
                return nums[i+1]
        if val == False:
            return nums[0]
        return -1