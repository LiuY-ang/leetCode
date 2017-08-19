# -*- coding:utf-8 -*-
import itertools
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans=0
        for point in points:
            d={}
            for ele in points:#统计到point距离相等的个数
                distance=(ele[0]-point[0])*(ele[0]-point[0])+(ele[1]-point[1])*(ele[1]-point[1])
                d[distance]=d.get(distance,0)+1
            for e in d:#排列
                ans=ans+d[e]*(d[e]-1)#n！/(n-m)!这里m为已知，m为2，化简后为n*(n-1)
        return ans

so=Solution()
print so.numberOfBoomerangs([[0,0],[1,0],[2,0]])
