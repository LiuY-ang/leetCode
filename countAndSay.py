class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        li=["","1","11","21","1211","111221"]
        if n>1 and n<=5:  #已经存储了，直接返回就可以了
            return li[n]
        for index in range(5,n):
            i=position=count=0
            say=""
            while  i < len(li[index]):
                if li[index][position] == li[index][i]: #数li[index][position]个数
                    count=count+1
                    i=i+1
                else:#数完之后
                    say=say+str(count)#拼接字符串
                    say=say+li[index][i-1]
                    count=0#进行下一次数个数的初始化
                    position=i
            say=say+str(count) #最外层循环结束后，没有拼接最后一次的字符串
            say=say+li[index][i-1]#所以拼接
            li.append(say)#添加
        return li[n]
solu = Solution()
print solu.countAndSay(7)
