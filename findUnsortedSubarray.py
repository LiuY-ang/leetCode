# -*- coding:utf-8 -*-
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        i,j=0,length-1
        while i+1<length and nums[i]<=nums[i+1]:#从前往后找到第一个逆序的
            i=i+1
        while j-1>=0 and nums[j]>=nums[j-1]:#从后往前找到第一个逆序的
            j=j-1
        print "i=",i,"j=",j
        ans=j-i+1#可能的未排序的数组长度
        if j==0 and i==length-1:#原数组为有序的
            return 0
        print nums[i:j+1]
        mini=min(nums[i:j+1])#取得nums中从i到j+1(不包括)位置上的最小元素
        maxi=max(nums[i:j+1])##取得nums中从i到j+1(不包括)位置上的最大元素
        #将可能乱序的子串排完序，然后分别向前检查，向后检查
        t=i-1#向前检查
        while t>=0 and nums[t]>mini:#前边的元素只要比最小值大，就接着往前检查
            t=t-1
            ans=ans+1
        t=j+1#往后检查
        while t<length and nums[t]<maxi:#后边的元素比maxi小，就往后检查
            t=t+1
            ans=ans+1
        return ans
so=Solution()
print so.findUnsortedSubarray([1,2,4,5,3])
