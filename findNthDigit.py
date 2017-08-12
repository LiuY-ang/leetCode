# -*- coding:utf-8 -*-
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=9:  #n<=9的话，那么直接返回
            return n
        s,i=0,0 #s存储数的个数。比如：10是两个数
        base=9
        while s<n:
            #base*pow(10,i)为(i+1)位数的个数，比如：2位数(10-99)的个数为90个数
            #base*pow(10,i)*(i+1)为(i+1)位数中数的个数
            #比如：2位数一共有90个数，数字的个数位90*2=180
            s=s+base*(i+1)
            base=base*10
            i=i+1
        i=i-1 #多加了一次1，减掉
        s=s-base/10*(i+1) #s也多加，减掉
        n=n-s #n减掉s，例如：n=30，s为9。n=n-s=21
        m=n%(i+1) #n对i+1,即位数，取余
        n=n/(i+1) #n除以位数，得到第几个数
        if m==0: #如果余数为0，则是第n个数
            x=n+pow(10,i)-1 #比如10是2两位数中的第一个数，11是第二个数
        else: #余数不为0的情况，则是第n+1个数
            x=n+pow(10,i) #得到数字
        digits=[] #存储各个位的位数
        while x!=0: #得到各个位上的数
            digits.append(x%10)
            x=x/10
        if m==0: #如果m==0，那么为个数数字
            return digits[0]
        return digits[len(digits)-m]



so=Solution()
print so.findNthDigit(11)
