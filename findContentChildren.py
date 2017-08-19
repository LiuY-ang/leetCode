# -*- coding:utf-8 -*-
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()#对s排序
        g.sort()#对g排序
        result,i,j=0,0,0#result存储结果，i为指向s元素的下标，j为指向g元素的下标
        while i<len(s) and j<len(g):
            if s[i]-g[j]>=0:#s为cookie的大小，g为孩子的最小需求；如果cookie的大小能够满足
                result+=1#孩子的需求，那么将result加1；并将i加1，j加1，以便比较下一个元素
                i+=1
                j+=1
            else: #s[i]-g[i]<0，即cookie的大小不满足孩子的最小需求，那么需要将cookie增大
                i+=1
        return result
so=Solution()
print so.findContentChildren([1,2],[1,2,3])
