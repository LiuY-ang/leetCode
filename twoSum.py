# -*- coding:utf-8 -*-
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0#初始化为第一个元素的下标
        j=len(numbers)-1 #初始化为最后一个元素的下标
        while i<j:
            if numbers[i]+numbers[j]==target: #如果相等
                return i+1,j+1#则直接返回
            elif numbers[i]+numbers[j]>target:#如果，前后两值的和大于terget
                j=j-1#则将后边的下标往前移，以减少两者的和
            elif numbers[i]+numbers[j]<target:#如果，前后两值的和小于terget
                i=i+1#则将前边的元素往后移，以增加两者的
so=Solution()
li=[2, 7, 11, 15]
print so.twoSum(li,13)
