class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index in range(0,len(nums)):
            if nums[index] >= target:
                return index
        return len(nums)

nums=[1,3,5,6]
solu=Solution()
print solu.searchInsert(nums,0)
