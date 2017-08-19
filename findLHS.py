# -*- coding:utf-8 -*-
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        d={}#用来存取某个数出现的次数
        m=0
        for i in nums:#统计数字的出现的次数
            d[i]=d.get(i,0)+1
        print d
        sortedNum=sorted(set(nums))#set(nums),如果nums中有负数，不能正确的排序
        print sortedNum
        i,pre=0,min(sortedNum)#pre用来村上一次访问的数
        for e in sortedNum:
            if e-pre==1 and d[e]+d[pre]>m:#e和pre差值相差为1，并且出现的次数较多
                m=d[pre]+d[e]
            pre=e
        return m
so=Solution()
print so.findLHS([1,3,2,2,5,2,3,7])
