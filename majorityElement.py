class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums)==1:
        #     return nums[0]
        nums.sort()
        return nums[len(nums)/2]
so=Solution()
print so.majorityElement([1,1,3])
