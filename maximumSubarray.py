class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        location=largeSum=nums[0]
        for index in range(1,len(nums)):
            location=max(location+nums[1],location)
            largeSum=max(location,largeSum)
        return largeSum
li=[-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print s.maxSubArray(li)
