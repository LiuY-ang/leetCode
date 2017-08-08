# -*- coding:utf-8 -*-
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroPos=0#zeroPos指向元素为0的下标
        for i in range(len(nums)):
            if nums[i]!=0:#如果不为0，那么把zeroPos指向的0元素交换
                temp=nums[i] #如果数组的前几个元素都不为0，那么zeroPos也会往后移动
                nums[i]=nums[zeroPos]
                nums[zeroPos]=temp
                zeroPos=zeroPos+1
            #如果nums[i]==0那么，只将i加1，以便找到非0数
so=Solution()
nums=[1,0,2,3,0,4]
so.moveZeroes(nums)
print nums
