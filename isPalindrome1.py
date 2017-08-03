class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_new = filter(str.isalnum,s).upper()
        return s_new == s_new[::-1]
