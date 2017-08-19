# -*- coding:utf-8 -*-
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n=bin(num)[2:]#变为二进制字符串
        print n
        s=""#存储结果
        for i in n:
            print i
            if i=='1':#把1变为0
                s=s+'0'
            else:#把0变为1
                s=s+'1'
        print s
        return int(s,2)#转为整数
so=Solution()
print so.findComplement(8)
