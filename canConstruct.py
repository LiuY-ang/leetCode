class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        se=set(ransomNote)
        print se
        for i in se:
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True
so=Solution()
print so.canConstruct("ab", "bab")
