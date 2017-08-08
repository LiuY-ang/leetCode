# -*- coding:utf-8 -*-
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        count=0
        isPrimes=[True]*n#建立n个元素的list
        isPrimes[0]=False
        isPrimes[1]=False
        #2,3 都是素数
        #print isPrimes
        q=int(math.sqrt(n)+1) #开方
        for i in range(2,q):
            if isPrimes[i]==True: #i是素数
                j=i*i #那么i*i不是素数，即j不是素数
                while j<n: #j+i=i*i+i=i*(i+1)也不是素数
                    isPrimes[j]=False
                    j=j+i
        #print isPrimes
        return sum(isPrimes)
so=Solution()
print so.countPrimes(3)
