# -*- coding:utf-8 -*-
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: #0不是2的幂
            return False
        while n!=1 and n%2==0: #n不为1，并且是2的倍数那么循环
            n=n/2
        print n
        if n>1: #循环结束，那么上面的两个条件某一个或者是二者某不满足
            return False
        else:
            return True
so=Solution()
print so.isPowerOfTwo(-16)
