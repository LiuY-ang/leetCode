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
        i=j=0 #i指向nums1，j指向nums2
        length=0
        while  i<m and j<n:
            if nums1[i] >= nums2[j]:
                t=m-1
                while t >= i: #nums1中的元素往后移，一遍腾出位置，给新元素
                    nums1[t+1]=nums1[t]
                    t=t-1
                nums1[i]=nums2[j] #添加新元素
                j=j+1
                i=i+1 #i 加1，因为添加了nums2中的一个新元素，添加到了nums1[i]位置
                m=m+1 #  m加1，因为有添加进一个新的元素
            else: #nums1[i] < nums2[j]
                i=i+1 #较小的元素已经在nums1中了，只需要将nums1中下标加1即可
            length=length+1
        if i < m: #此时什么也不用做，因为以合并到nums1中去
            pass #剩下的数就在nums1中
        if j < n:
            while j<n:
                nums1[length]=nums2[j]
                j=j+1
                length=length+1

so=Solution()
list1=[1,2,4,5,6,0]
list2=[3]
so.merge(list1,5,list2,1)
print list1
