#-*- coding: UTF-8 -*-
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums=nums1[0:m]
        nums1=[]
        i=j=length=0
        while i<m and j<n:
            if nums[i] <= nums2[j]:
                nums1.insert(length,nums[i])
                i=i+1
            else: #nums[i]>nums2[j]
                nums1.insert(length,nums2[j])
                j=j+1
            length=length+1
        if i<m:
            print "------"
            while i<m:
                nums1.insert(length,nums[i])
                i=i+1
                length=length+1
        if j<n:
            print "++++++"
            while j<n:
                print "++++++=== ",length,nums2[j]
                nums1.insert(length,nums2[j])
                length=length+1
                j=j+1
        nums1=nums1
so=Solution()
list1=[0]
list2=[1]
so.merge(list1,0,list2,1)
print list1
