# -*- coding:utf-8 -*-
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        '''
        枚举小时h和分钟m，然后判断二进制1的个数是否等于num
        '''
        ans = []
        for h in range(12):#枚举小时
            for m in range(60):#枚举分钟
                if (bin(h) + bin(m)).count('1') == num:#判断1的个数
                    ans.append('%d:%02d' % (h,m))
        return ans
