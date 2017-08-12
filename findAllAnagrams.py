# -*- coding:utf-8 -*-
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        #代码的整理和解释在findAllAnagrams1.py中
        result=[]
        i=0
        slength,plength=len(s),len(p)
        while i < len(s):
            print i
            if self.detectAnagram(s,p,i) == True:
                result.append(i)
            if i+plength<slength and s[i+plength] not in p:
                i=i+len(p)+1
            elif i+plength<slength and s[i]==s[i+plength]:
                i+=1
                while i+plength<slength and s[i]==s[i+plength]:
                    print "---"
                    result.append(i)
                    i+=1
            elif i+plength>slength:
                break
            else:
                i=i+1
        return result

    def detectAnagram(self,s,p,pos):
        temp=s[pos:pos+len(p)]
        if set(temp)!=set(p) or len(temp)!=len(p):
            return False
        # if len(set(temp))==len(set(p)): #没有重复元素
        #     print "***"
        #     return True
        for e in set(temp):
            if temp.count(e)!=p.count(e) : #如果统计为0
                return False
        return True
so=Solution()
print so.findAnagrams("abcdabcd","abcd")
