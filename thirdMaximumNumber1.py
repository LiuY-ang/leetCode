class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums)if len(set(nums))<3 else sorted(set(nums))[-3]
so=Solution()
print so.thirdMax([1,2,2])
