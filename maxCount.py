# -*- coding:utf-8 -*-
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        r,c=m,n
        for e in ops:
            if r>e[0]:#行比较，取行元素最小
                r=e[0]
            if c>e[1]:#列比较，取列元素最小
                c=e[1]
        return r*c
so=Solution()
print so.maxCount(18,3,[])
