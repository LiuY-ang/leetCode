class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numsLength=len(nums)
        k=k%numsLength;
        nums=nums[-k:]+nums[:-k]
        print nums


so=Solution()
so.rotate([1,2,3,4,5,6,7],3)
