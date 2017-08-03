class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #  A XOR A = 0 and the XOR operator is commutative
        xor_result = 0
        for a_num in nums:
            xor_result ^= a_num
        return xor_result
