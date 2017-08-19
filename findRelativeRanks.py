# -*- coding:utf-8 -*-
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        temp=["Gold Medal", "Silver Medal", "Bronze Medal"]
        result=[""]*len(nums)#result存储结果
        d={}
        ranks=sorted(nums)[::-1]#排序，并倒置拍完序的数组
        for i in range(len(nums)):#存下nums[i]在nums中的位置
            d[nums[i]]=i
        print d,ranks
        for i in range(len(ranks)):
            position=d[ranks[i]] #得rank[i]原先的位置
            print position
            if i<3:
                result[position]=temp[i]
            else:
                result[position]=str(i+1)
        return result
so=Solution()
print so.findRelativeRanks([1,2,3,4,5])
