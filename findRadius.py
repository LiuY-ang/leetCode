#-*- coding:utf-8 -*-
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houseLength=len(houses)
        heaterLength=len(heaters)
        if houseLength==1 and houses[0]<=heaters[0]:
            return heaters[0]-houses[0]
        if heaters==1:
            return max(houses)-heaters[0]
        side,pre=[],houses[0] #记录暖炉的左右房子的距离;pre记录上一个暖炉所在的位置
        i,j=0,0
        while i<houseLength and j<heaterLength:
            print i,j,pre
            if houses[i]==heaters[j]:
                side.append(houses[i]-pre)
                if i+1<houseLength:
                    pre=houses[i+1]#houses访问有可能会越界,更新pre,用以记录上一个房子所在的位置
                else:
                    pre=houses[i]
                i,j=i+1,j+1
            elif houses[i]<heaters[j]:
                i=i+1
            elif houses[i]>heaters[j]:#暖壶在两个房子中间
                side.append(abs(heaters[j]-pre))
                pre=houses[i]#pre记录上一个房子的位置
                j=j+1
        print side
        if j!=heaterLength:#暖炉更远
            side.append(min(houses[i-1]-heaters[j-1],heaters[j]-houses[i-1]))
        if i!=houseLength:#房子更远
            side.append(houses[-1]-heaters[-1])
        print side #打印暖炉两边的房子距离
        k,sideLength=1,len(side)
        mini=max(side[0],side[-1])
        while k<sideLength-1:
            if side[k]%2==0:
                radius=side[k]/2
            else:
                radius=side[k]/2+1
            if radius>mini:
                mini=radius
            k=k+1
        return mini

so=Solution()
print so.findRadius([1,2,3,4],[1,4])
