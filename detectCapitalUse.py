# -*- coding:utf-8 -*-
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() or word.isupper():#判读是否全部为大写或者全部为小写
            return True
        #其余的情况
        firstChar=word[0]#取得第一个字符
        leftChar=word[1:]#取得剩下的字符
        print firstChar,leftChar
        #如果第一个字符为大写，剩下的为小写，返回True
        if firstChar.isupper() and leftChar.islower():
            return True
        return False
so=Solution()
print so.detectCapitalUse("FlaG")
