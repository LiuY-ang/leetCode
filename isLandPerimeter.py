# -*- coding:utf-8 -*-
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result=0
        for g in range(len(grid)):
            for e in range(len(grid[g])):
                if grid[g][e]!=0:
                #依次接下来检查上下左右
                    if g-1>=0 and grid[g-1][e]!=1:#检查上边，g-1>=0保证上边存在
                        result+=1
                    elif g-1<0 :#如果上边不存在的话也加1
                        result+=1
                    if g+1<len(grid) and grid[g+1][e]!=1:#检查下边,g+1<len(grid)保证下边存在
                        result+=1
                    elif g+1>=len(grid):#如果下边不存在的话，加1
                        result+=1
                    if e-1>=0 and grid[g][e-1]!=1:#检查左边,e-1>=0保证存在
                        result+=1
                    elif e-1<0:#如果不存在的话，也进行加1操作
                        result+=1
                    if e+1<len(grid[g]) and grid[g][e+1]!=1:#检查右边，e+1<len(gird[g])保证右边存在
                        result+=1
                    elif e+1>=len(grid[g]):#不在的话加1
                        result+=1
        return result
so=Solution()
grid=[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print so.islandPerimeter(grid)
