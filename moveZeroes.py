class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # print range(len(nums))
        length=len(nums)
        i=0
        while i < len(nums):
            if nums[i]==0:
                nums.pop(i)#删除该位置上的0
            else:
                i+=1
        while len(nums)<length: #把删掉的0，在添加到最后
            nums.append(0)

so=Solution()
nums = [0,0,1]
so.moveZeroes(nums)
print nums
