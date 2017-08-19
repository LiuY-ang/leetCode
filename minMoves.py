class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        nums.sort()
        n=len(nums)-1
        while n>0:
            s=s+nums[n]-nums[0]
            n=n-1
        return s
so=Solution()
print so.minMoves([1,2,4])
