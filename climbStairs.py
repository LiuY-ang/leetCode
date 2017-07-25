class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
      	k=1
      	m=2
      	if n==1:
      		return k
      	if n==2:
      		return m
      	for i in range(3,n+1):
      		t=k+m
      		k=m
      		m=t
      	return m