# -*- coding:utf-8 -*-
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a==b:#如果相等
            return -1#那么不存在
        #执行到这那么说明a和b是不相等的，只需要返回a，b较长的长度即可
        alength=len(a)#得到a的长度
        blength=len(b)#得到b的长度
        return alength if alength>=blength else blength
