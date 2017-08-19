# -*- coding:utf-8 -*-
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length=len(nums)#得nums的长度
        origin=range(1,length+1)#得到原来的nums
        loss=list(set(origin)-set(nums))[0]#得到丢失的数
        diff=sum(origin)-sum(nums)#得到多的数和丢失的数之间的差值
        return loss-diff,loss
so=Solution()
print so.findErrorNums([1,2,2,4])
