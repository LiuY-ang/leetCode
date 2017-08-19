# -*- coding:utf-8 -*-
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        理解题意
        '''
        i=0
        result=[]
        while i<len(findNums):
            j,position=0,0
            while j<len(nums):
                if findNums[i]==nums[j]:#在nums中找到findNums[i]的位置
                    position=j#标记该位置
                    break#结束循环
                j+=1
            while j<len(nums):
                if nums[position]<nums[j]:#找到第一个大于findNums[i]的数就停止
                    result.append(nums[j])
                    break
                j+=1
            if j==len(nums):#如果j执行到最后，代表没有找到
                result.append(-1)#添加-1
            i=i+1
        return result
so=Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print so.nextGreaterElement(nums2,nums1)
