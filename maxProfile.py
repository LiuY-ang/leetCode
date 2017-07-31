class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1: #如果元素个数小于等于1个
            return 0 #直接放回0
        rear=1#循环之前都是进行初始化
        front=0
        maxP=0#代表最大利润
        while rear<len(prices):
            nowP=prices[rear]-prices[front] #当前的利润，不一定是最大的
            if nowP<=0: #如果当前利润小于0，即prices[rear]-prices[front]<=0
                front=rear #移项之后为prices[rear]<=prices[front],后边的元素（价格）更小
                rear=rear+1#那么将rear赋值给front，rear加1，接着检查后边的元素
            if nowP>0:#当前元素大于0
                if maxP<nowP: #并且nowP>maxP
                    maxP=nowP#那么更改最大利润的值
                rear+=1
        return maxP
so=Solution()
print so.maxProfit([3,3])
