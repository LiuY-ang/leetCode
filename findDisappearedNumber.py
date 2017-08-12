# -*- coding:utf-8 -*-
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length=len(nums)#记录下去重之前nums的长度
        nums.sort()#排序
        nums=list(set(nums)) #去重
        result=[] #保存结果
        i,count=0,1 #i为下标，count为i位置上应该出现的数字
        while i<len(nums):
            if nums[i]!=count: #如果没有i的位置上，没有出现该出现的位置
                result.append(count) #将该没有出现的数字添加到结果集中
                i=i-1 #使其下一次循环还停留在该位置上，然后在循环的最后在加，i还是处在原来的位置
            count+=1 #下一次应该出现的数字
            i+=1#下标加1
        i=count #防止出现[1,2,2,2]这样的情况
        while i<=length:
            result.append(i)
            i+=1
        return result
so=Solution()
print so.findDisappearedNumbers([1,2,2,2])
