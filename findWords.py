# -*- coding:utf-8 -*-
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        oneLine="eiopqrtuwyQWERTYUIOP" #存储最上边的元素，包括大小写
        twoLine="adfghjklsASDFGHJKL"
        threeLine="bcmnvxzZXCVBNM"
        levels=["",oneLine,twoLine,threeLine]
        i=0
        while i<len(words):
            #print i,words[i]
            level=0#存储words[i]属于键盘上的第几层
            if words[i][0] in oneLine:
                level=1
            elif words[i][0] in twoLine:
                level=2
            elif words[i][0] in threeLine:
                level=3
            temp=0#指向words[i]中元素的下标
            print "level=",level
            while temp < len(words[i]):
                print words[i][temp]
                if words[i][temp] in levels[level]: #如果word[i][temp]在相应的levels[level]
                    temp+=1#则继续循环
                else:#如果某一个元素不在特定的某一行中，那么结束循环
                    break
            print temp
            if temp==len(words[i]):#temp依次执行循环，执行到来最后，说明word[i]中的元素都在某一行中
                i+=1
            else:#如果words[i]中的元素有在别的行的，那么把该元素words[i]删除
                words.pop(i)
        return words
so=Solution()
print so.findWords(["Hello","Alaska","Dad","Peace"])
