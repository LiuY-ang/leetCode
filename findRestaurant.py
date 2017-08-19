# -*- coding:utf-8 -*-
import sys
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common=set(list1) & set(list2)
        common=list(common)#得到共同的餐厅
        ans,mini=[],sys.maxint
        for e in common:
            s=list1.index(e)+list2.index(e)#比较每个餐厅是
            if s<mini:#比较餐厅是否更小
                mini=s
                ans=[e]
            elif s==mini:
                ans.append(e)
        return ans
so=Solution()
list1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2=["KFC", "Shogun", "Burger King"]
print so.findRestaurant(list1,list2)
