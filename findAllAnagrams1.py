# -*- coding:utf-8 -*-
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result=[] #用来存储结果
        i=0 #遍历开始的下标
        slength,plength=len(s),len(p) #得到两者的长度
        while i < slength:
            print i
            if self.detectAnagram(s,p,i) == True: #检测从i开始的，plength个元素是否为Anagram
                result.append(i) #是的话，添加到result中
            #以下为改变下标i
            if i+plength<slength and s[i+plength] not in p:#比如：s='abceabc',p='abc'
                i=i+plength+1 #那么直接将i改为i+plength+1,因为e不在p中，i只要小于i+plength+1都不会相等
            elif i+plength<slength and s[i]==s[i+plength]:#该条主要判断s中有循环的情况，比如：
                i+=1#s="abcdabcdabcdabcdabcd",p="abcd"；处理这种情况，依次将i往后移，并添加到result中
                while i+plength<slength and s[i]==s[i+plength]: #直到i+plength<slength或者s[i]==s[i+plength]
                    result.append(i) #两者之一不满足，退出循环
                    i+=1
            elif i+plength>slength: #这条判断s从位置i开始不能取plength个元素了，那么直接结束
                break
            else: #其余情况简单的将i加1
                i=i+1
        return result

    def detectAnagram(self,s,p,pos):
        temp=s[pos:pos+len(p)] #取得从pos到pos+len(p)之间的元素，不包括pos+len(p)位置上元素
        if set(temp)!=set(p) or len(temp)!=len(p): #如果把重复元素去掉之后，长度不相等或者
            return False #不去重两者的长度就不相等，那么直接返回False值
        for e in set(temp): #元素去重，并依次取出里面的元素
            if temp.count(e)!=p.count(e) : #如果某一元素在temp和p中的个数不相等
                return False#返回false值
        return True#执行到这，说明是Anagram
so=Solution()
print so.findAnagrams("abcdabcd","abcd")
