# -*- coding:utf-8 -*-
import sys
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i,m,length=0,float("-inf"),len(nums)
        s,pre,n=sum(nums[i:i+k]),0,0#s存储s[i,i+k]的和，初始为前k的和
        #n存储为下一个即将要访问的数，pre存储为i位置的数，即要放弃访问的数，初始化为0
        while i+k<length:
            s=s-pre+n#计算本次循环和的值
            average=1.0*s/k#求的平均值
            print "average=",average,"s=",s
            if average>m:
                m=average
            pre,n=nums[i],nums[i+k]#更新pre和n
            i=i+1
        print pre,n
        average=1.0*(s-pre+n)/k#计算最后k个数的平均值
        if average>m:
            m=average
        return m
so=Solution()
print so.findMaxAverage([1,12,-5,-6,50,3],4)
