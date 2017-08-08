class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        n=len(nums)+1
        for i in nums:
            s+=i
        return n*(n-1)/2-s #数列和减去nums中数的和就是漏掉的数
so=Solution()
print so.missingNumber([1,0,3])
