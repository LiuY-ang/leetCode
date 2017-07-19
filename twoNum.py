class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        d = {}
        index = 0
        while index < length:
            if d.get(target-nums[index],-1) == -1:
                #若target-nums[index]不在d中，则把nums[index]添加到d,方便快速访问
                d[nums[index]] = index
                index = index + 1 #下标加1，老以为是c语言中，自动加1
            else:
                return d.get(target-nums[index]),index  #返回下标
