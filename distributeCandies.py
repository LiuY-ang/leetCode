# -*- coding:utf-8 -*-
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        length=len(candies)#糖果的个数
        setLength=len(set(candies)) #表示糖果的种类
        if setLength>=length/2:#糖果的种类大于等于应该得到的糖果数
            return length/2#那么分得的糖果的种数个数为得到的糖果数，即糖果都不重样
        else: #setLength<length/2，即糖果的种类少于应该得到糖果数
            return setLength#最多拥有的糖果数为种类数
