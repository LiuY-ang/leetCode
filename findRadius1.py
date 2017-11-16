#-*- coding:utf-8 -*-
import sys
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        print houses
        print heaters
        houseLength=len(houses)
        heaterLength=len(heaters)
        preHeater,preHouse,i,j,maxRadius=heaters[0],houses[0],0,0,-1
        radiuses,d=[],{}
        while i<houseLength and houses[i]<heaters[j]:#第一个暖炉在房子的中间
            d[houses[i]]=heaters[j]-houses[i]
            i=i+1
        if i!=0:
            i=i-1
        while j<heaterLength and heaters[j]<houses[i]:
            d[houses[i]]=min(d.get(houses[i],sys.maxint),abs(houses[i]-heaters[j]))
            preHeater=heaters[j]
            j=j+1
        if j!=0:
            j=j-1
        print preHeater,i,j
        while i<houseLength and j<heaterLength:
            print 'i=',i,'j=',j,'preHeater=',preHeater
            if houses[i]>heaters[j]:#暖炉在某个房子的位置上
                preHeater=heaters[j]#更新上一个暖炉的位置
                if j+1<heaterLength :
                    j=j+1
            m=min(abs(houses[i]-preHeater),abs(heaters[j]-houses[i]))
            d[houses[i]]=min(d.get(houses[i],sys.maxint),m)
            i=i+1
        print d
        for k in d:
            if d[k]>maxRadius:
                maxRadius=d[k]
        return maxRadius
so=Solution()
print so.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]),'--'
