# -*- coding:utf-8 -*-
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[1],nums[0])
        nowCount=[nums[0]]
        maxCount=0
        if nums[0]>nums[1]:
            nowCount.append(nums[0])
            maxCount=nums[0]
        else: #nums[0]<=nums[1]
            nowCount.append(nums[1])
            maxCount=nums[1]
        for i in range(2,len(nums)):
            temp=max(nums[i]+nowCount[i-2],nowCount[i-1])
            nowCount.append(temp)
            if temp>maxCount:
                maxCount=temp
        return maxCount
so=Solution()
print so.rob([1,2,3])
