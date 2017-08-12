# -*- coding:utf-8 -*-
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=set(nums)
        result=[]
        for i in range(1,len(nums)+1):
            if i not in n:
                result.append(i)
        return result

so=Solution()
print so.findDisappearedNumbers([1,2,2,2])
