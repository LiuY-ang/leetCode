class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numStr=""
        Max=0
        for i in nums:
            numStr=numStr+str(i)
        numbers=numStr.split("0")
        for e in numbers:
            if len(e)>Max:
                Max=len(e)
        return Max
so=Solution()
print so.findMaxConsecutiveOnes([0])
