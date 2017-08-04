# -*- coding：utf-8 -*-
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ns=bin(n)[2:] #转换为二进制，转换后二进制的前两位为‘0b’，所以从第三位取
        #print len(ns),"  ",ns
        while len(ns)<32: #如果不足32位
            ns='0'+ns#则进行添0处理
        #print len(ns),"  ",ns
        #print int(ns[::-1],2)
        return int(ns[::-1],2)#进行逆置处理，并把逆置后的二进制字符串转换为十进制
                              #第二个参数代表原数是多少进制表示的
so=Solution()
so.reverseBits(43261596)
