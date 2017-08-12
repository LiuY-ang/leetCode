# -*- coding:utf-8 -*-
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        li=[]
        d={}
        j=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j] and d.get(j,-1)==-1 : #如果在nums2中找到某个值和nums1[1]相等
                    li.append(nums1[i]) #并且该位置的数字没有被标记过
                    d[j]=True #标记该位置的被访问过
                    break #结束本次循环
        return li
so=Solution()
nums1=[61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81]
nums2=[5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]

print so.intersect(nums1,nums2)
