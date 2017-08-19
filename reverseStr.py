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
        for i in range(0,length,k):
            print i,isReverse
            if isReverse==True:
                result+=s[i:i+k][::-1]#反转从i到i+k之间的元素
            else:
                result+=s[i:i+k]#不反转
            isReverse=not isReverse
        return result
so=Solution()
print so.reverseStr("abcdef",3)
