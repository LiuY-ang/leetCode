# -*- coding:utf-8 -*-
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        if length==3:#如果数组的长度为3，那么直接返回
            return nums[-1]*nums[-2]*nums[-3]
        nums.sort()
        print nums
        positive,negative,zero=0,0,False#用以统计正数，负数的个数，其zero用来标记
        for e in nums: #是否有0
            if e>0:
                positive+=1
            elif e<0:
                negative+=1
            else: #e==0
                zero=True
        if positive>=3:#如果正数的个数大于等于3个。那么最大的乘积有可能出现在2个地方
            last=nums[-1]*nums[-2]*nums[-3] #最后3个数的乘积
            notAllLast=nums[-1]*nums[0]*nums[1]#最后一个数和最小的两个负数的乘积
            return last if last>=notAllLast else notAllLast
        elif positive==2 or positive==1: #如果正数的个数为1个或者2个
            return nums[-1]*nums[0]*nums[1] #那么最大的乘积为最大的正数和最小的两个负数的积
        elif zero: #如果正数个数为0，且有0，直接返回0
            return 0
        else: #全是负数，返回最大的三个负数之积
            return nums[-1]*nums[-2]*nums[-3]
so=Solution()
print so.maximumProduct([1,2,3,4])
