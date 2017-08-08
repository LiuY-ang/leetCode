class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        di={}
        length=len(nums)
        for ele in nums:
            if di.get(ele,-1)==-1:
                di[ele]=True
            else:
                return False
        return True
