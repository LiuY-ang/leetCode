#-*- coding: UTF-8 -*- 
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climb_stairs(0,n)#第一个参数代表还没有迈出第一步
    def climb_stairs(self,i,n):
        if( i>n): #如果在最后了2步之后，超出n的值，则证明这走法不合适，不是一种走法
            return 0
        if( i==n):#正好相等，则是一种走法，返回1
            return 1
        step1=self.climb_stairs(i+1,n) # 下一次走一步
        step2=self.climb_stairs(i+2,n)# 下一次走两步
        print step1,step2
        return step1+step2
so = Solution()
print so.climbStairs(5); #当n=35的时候就超时了
#暴力破解
#一遍一遍的去模拟过程
