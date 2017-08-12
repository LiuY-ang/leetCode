class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums))<3:
            return max(nums)
        nums.sort()
        nums=nums[::-1]
        print nums
        pre=-1
        j,i=-1,0
        while i<len(nums) and j<2:
            if pre!=nums[i]:
                pre=nums[i]
                j=j+1
            i=i+1
        i=i-1
        return nums[i]
so=Solution()
print so.thirdMax([1,2,2])
