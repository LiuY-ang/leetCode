# -*- coding:utf-8 -*-
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()#排序
        ans=0
        for index in range(0,len(nums),2):#隔一个数取一个数，这样得到的和是最大的
            print index
            ans=ans+nums[index]
        return ans
so=Solution()
print so.arrayPairSum([1,4,3,2])
