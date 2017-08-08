# -*- coding:utf-8 -*-
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        #检查同一个键是否映射到同一个值
        #例如 s='aa'  t='ab'
        for i in range(len(t)):
            if s[i] not in d:
                d[s[i]] = t[i]
            # check if mapping is correct
            elif d[s[i]] != t[i]:
                return False

        # check if multiple characters mapped to same character
        #检查不同的键是否映射到同一个值，例如：s='ab' t='aa'。这对s，t能够通过上边的循环
        temp = set([])
        for k in d:
            if d[k] in temp:
                return False
            temp.add(d[k])
        return True
