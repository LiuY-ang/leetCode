# -*- coding:utf-8 -*-
import sys
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minStack=[] #最小值数组，栈顶元素为最小的值


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        #如果最小值数组为空，或者最小值数组的栈顶的元素大于等于要入栈的元素
        #则将该元素也入最小栈中
        #入栈：-2，0，-3                  出栈：-3        最小值为-2 ：这是大于的作用
        #入栈：2，1，1，-2                 出栈：-2    最小值为1  出栈1后  最小值为1 ：这是等于的作用
        if len(self.minStack)==0 or self.minStack[-1]>=x:
            self.minStack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        last=self.top()#得到栈顶元素
        self.stack.pop() #删除栈的最后一个元素
        #如果删除的元素等于最小栈的栈顶元素，那么最小栈的栈顶元素也需要删除，因为已经不是最小的元素了
        if last==self.minStack[-1]:
            self.minStack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] #得到最后一个元素


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minStack)!=0: #最小值的栈非空，那么返回栈顶元素
            return self.minStack[-1]
        return None#若为空，则返回空

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print obj.getMin()
obj.pop()
print obj.top()
print obj.getMin()
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
