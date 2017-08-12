# -*- coding:utf-8 -*-
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=str.split()
        length=len(pattern)
        if length!=len(s):#如果分离str返回的list的长度和pattern长度不等
            return False
        d={}
        #保证不同的值映射到不同的值上
        for i in range(length):
            print pattern[i]
            if d.get(pattern[i],-1)==-1:
                d[pattern[i]]=s[i]
            elif d.get(pattern[i])!=s[i]: #存在的话
                return False
        value=[]
        #保证不同的值不会映射到同一个值上；pattern='ab',str='a a'
        for k in d:
            if d[k] in value:
                return False
            value.append(d[k])
        return True
so=Solution()
print so.wordPattern("jquery","jquery")
