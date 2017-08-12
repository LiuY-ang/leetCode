class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        min1,min2,max1,max2,max3=nums[0],nums[1],nums[-1],nums[-2],nums[-3]
        return max(min1 * min2 * max1, max1 * max2 * max3)
