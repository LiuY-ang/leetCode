#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
s = raw_input()
snum = string.split(s,' ')
nums = []
for x in snum:
    nums.append(int(x))
key = nums[-1]
length = len(nums)
nums = nums[0:length-1]
print nums,key
flag = 0
ix = 0
iy = 0
for x in nums:
    for y in nums:
        if x==y and flag == 0:
            pass
        elif x+y==key and flag == 0:
            print ix,iy
            flag = 1
        if nums[iy] == nums[len(nums)-1]:
            iy = 0
            ix = ix +1
        else:
            iy = iy + 1
