# -*- coding:utf-8 -*-
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        length=len(nums)
        number=0
        numberLength=0
        for i in range(0,length):
            if count.get(nums[i],-1)==-1:#不存在的话
                count[nums[i]]=1#那么添加到count中
                if count[nums[i]]>length/2 :
                    return nums[i]
            else: #如果存在的话
                count[nums[i]]=count[nums[i]]+1 #将出现的次数加1
                if count[nums[i]]>length/2 : #探测到某个数出现的次数较多
                    return nums[i]
        return number


so=Solution()
print so.majorityElement([1,2])
