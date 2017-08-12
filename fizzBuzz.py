# -*- coding:utf-8 -*-
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        li=[]
        for i in range(n):
            print i
            if (i+1)%3==0 and (i+1)%5==0: #既能被3整除，也能被5整除
                li.append("FizzBuzz")
            elif (i+1)%3==0: #只能被3整除
                li.append("Fizz")
            elif (i+1)%5==0: #只能被5整除
                li.append("Buzz")
            else: #添加数字的字符串
                li.append(str(i+1))
        return li
so=Solution()
print so.fizzBuzz(10)
