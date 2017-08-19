# -*- coding:utf-8 -*-
import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        '''
        We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
        完美数为其所有的正整数因子之和（除该数之外）为本数。28的因子有1,2,4,7,14。这些因子的和为28。
        '''
        if num<=1:#num小于等于1，都是不符合完美数的定义。完美数首先是一个正数
            return False
        s,i=1,2
        n=math.sqrt(num)#取得num的开平方之后的数。借鉴了判断素数的过程
        while i<=n:
            if num%i==0:#没有余数
                # print i,num/i #那么i和num/i都是num的因子
                s=s+i+num/i
            i+=1
        if s==num:#循环结束之后，s==num证明为perfect num
            return True
        return False
so=Solution()
print so.checkPerfectNumber(28)
