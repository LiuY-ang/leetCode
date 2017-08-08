# -*- coding:utf-8 -*-
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s))!=len(set(t)): #如果拥有的元素就不一样的话
            return False #直接返回
        length=len(s)
        di={} #建立一个dict，其中s[i]为键，t[i]为值
        i=0 #下标从0开始
        while i<length:
            #print i
            if di.get(s[i],-1)==-1: #如果不存在s[i]->t[i]
                di[s[i]]=t[i] #则建立该种映射关系
            else: #已经存在某种映射的关系
                tt=di.get(s[i]) #取出该值
                if tt==t[i]: #该值如果和t[i]相等
                    pass#则不做处理
                else: #如果以前的映射值和当前的值不相等
                    return False
            i+=1
        return True
so=Solution()
print so.isIsomorphic("add","egg")
