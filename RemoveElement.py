class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index=0
        while( index < len(nums) ):
            if nums[index] == val:
                nums.pop(index)
            else:
                index=index+1
        return len(nums)
li=[3,3]
sol = Solution()
length = sol.removeElement(li,3)
print li
