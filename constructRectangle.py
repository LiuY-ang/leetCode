# -*- coding:utf-8 -*-
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        i,length=area,area#i指向较大的数，从后往前
        j,width=1,1#j指向较小的数，从前往后
        while i>=j:
            print "i=",i,"j=",j
            if i*j==area:#如果i*j==area
                if i-j<length-width:#判断长度和宽度之差是否更小
                    length=i#更小的话更新长度和宽度
                    width=j
                j=j+1#将较小的数变大
                i=i-1#将较大的数变小
            elif i*j>area:#i*j大于area,需要将i*j减小，即需要将i变小
                i=area/j#使其变化加快，area/j得到的值只有整数部分，area/j<=真实的area/j(不只取整数，有可能是分数)
            elif i*j<area:
                j=j+1 #使其变化慢一些,j是连续变化的
        return length,width
so=Solution()
print so.constructRectangle(12)
