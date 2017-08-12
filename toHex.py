# -*- coding:utf-8 -*-
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        isNegative=False
        if num<0: #如果为负数,用补码的形式该数。求该负数的补码
            num=4294967296+num #pow(10,32)=4294967296，num本身为负数
        he=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        h=[] #变成16进制的补码
        while num>=16:
            h.append(he[num%16])
            num=num/16
        h.append(he[num%16])
        print h[::-1] #逆置数组
        return "".join(h[::-1]) #变成字符串
so=Solution()
print so.toHex(-2)
