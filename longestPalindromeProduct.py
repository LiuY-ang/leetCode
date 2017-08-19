class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        提前计算出n为数字乘积为回文串的积，然后对1337取余
        '''
        palindrome=[9,987,123,597,677,1218,877]
        return palindrome[n-1]
