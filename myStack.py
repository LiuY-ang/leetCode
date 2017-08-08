class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop(len(self.stack)-1)


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.stack)>0:
            top=len(self.stack)-1
            return self.stack[top]
        return None


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.stack)==0:
            return True
        return False



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print param_2
print param_3
print param_4
