# -*- coding:utf-8 -*-
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length=len(s)
        if length<=k:
            return s[::-1]
        result,isReverse="",True
        for i in xrange(0,length,2*k):
            print i,isReverse
            result=result+s[i:i+k][::-1]
            result=result+s[i+k:i+2*k]
        return result
so=Solution()
print so.reverseStr("abcdef",2)
