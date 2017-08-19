# -*- coding:utf-8 -*-
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0: #n为需要种植的花的个数，个数为0，说明不需要种植
            return True
        i,length=0,len(flowerbed)
        flowerbed.append(0)#在flowerbed的最后添加0，这样便于操作。主要便于操作最前边和最后边有0的情况
        while i<length and n!=0:
            if flowerbed[i]==1:#如果flowerbed[i]==1，那么下一个位置不管是0还是1，都不符合条件
                i=i+2#所以直接检查(i+2)的位置
            elif flowerbed[i-1]==0 and flowerbed[i+1]==0:#flowerbed[i]==0并且前后都为0，那么这个位置可以种植
                flowerbed[i]=1#将该位置种上花
                i,n=i+2,n-1#那么下一个位置也是不符合条件的，直接检查(i+2)位置，并将需要种植的个数减1
            else:#其余的情况，检查(i+1)位置
                i=i+1
        if n==0:#循环结束，检查n是否为0，为0说明可以种植n颗花
            return True
        return False#否则，不能种植n颗花
so=Solution()
flowerbed = [0,0,1,0,0,0,1,0,0]
n = 3
print so.canPlaceFlowers(flowerbed,n)
