#-*- coding: UTF-8 -*-
# 方法二
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        li={} #存储已经探明的台阶走法的种数
        return self.climb_stairs(0,n,li)
    def climb_stairs(self,i,n,li):
        if i>n:  #在迈出最后一步（可能是一个台阶，两个台阶）之后，如果超过
            return 0 #则表示这种走台阶的方法是不可行的
        elif i==n: #若相等，则表示该种走台阶的方法是可行的
            return 1 #故返回1，代表一种走法
        elif li.get(i,-1) != -1: #若第i个台阶到到台阶顶的种数存在，
            return li.get(i) #则直接返回该种数
        step1=self.climb_stairs(i+1,n,li) #试探只走一个台阶的情况
        step2=self.climb_stairs(i+2,n,li) #试探走两个台阶的情况
        li[i] = step1+step2 #存储第i个台阶走到台阶顶的走法种数
        return li.get(i)
so = Solution()
print so.climbStairs(35);
#当n等于5的时候，若递归到i=3
# i=3,下一步递归i+1,i+1的值为4，
    # i=4,下一步递归i+1,i+1的值为5，满足i==n的情况，返回1
    # i=4,然后在递归i+2,i+2的值为6，满足i>n的情况，放回0
    # i=4,设置li[i]=step1+step2,即为li[4]=step1+step2=1+0=1,返回
#i=3，下一步递归i+2，i+2的值为5，
    #i=5,满足递归条件i==n,返回1
#i=3，li[i]=step1+step2,即li[3]=step1+step2=1+1=2
