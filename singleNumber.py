# -*- coding:utf-8 -*-
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dist={}
        s=0
        iSum=0
        for i in nums:
            s+=i
            if dist.get(i,-1)==-1: #不存在的话
                dist[i]=True
                iSum=iSum+i*2
        return iSum-s
so=Solution()
print so.singleNumber([2,2,3,3,4,4,5])
