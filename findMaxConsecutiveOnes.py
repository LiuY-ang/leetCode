# -*- coding:utf-8 -*-
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max,count=0,0
        for i in range(len(nums)):
            if nums[i]!=1:#如果1出现中断
                if count>Max: #当前的‘1’的个数比前边的已知的连续’1’的个数多
                    Max=count #更新Max
                    count=-1 #计数清零，这里赋值-1，是因为后边接着加1，就变为了0
                else: #count<=Max
                    count=-1
            count+=1 #计数加1
        if count>Max: #最后的count直接结束了，没有比较。在此比较
            Max=count
        return Max
so=Solution()
print so.findMaxConsecutiveOnes([1,0,0,1,1])
