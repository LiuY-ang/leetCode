# -*- coding:utf-8 -*-
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        hm = {}
        for i in nums1:
            hm[i] = hm.get(i,0) + 1 #统计nums1中元素出现的次数
        l = []

        for i in nums2:
            if i in hm and hm[i]: # i in hm and hm[i]!=0，i在hm中存在键，并且该键的值不为0
                l.append(i)
                hm[i] -= 1
        return l
