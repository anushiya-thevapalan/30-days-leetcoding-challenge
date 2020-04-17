'''
Day 17 - 30 days Leetcoding Challenge - April 17, 2020

Problem (leetcode: 200)

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land = set()
        
        #Put all pieces of land in a set
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    land.add((row, column))
        islands = 0
        
        #If the piece of land is still in the
        #set we have not explored it yet. If
        #a piece of land we try to explore is
        #not in the set, we have already explored
        #it so we do nothing or it is water.
        def explore(r, c):
            if (r,c) in land:
                land.remove((r,c))
                explore(r, c+1)
                explore(r, c-1)
                explore(r+1, c)
                explore(r-1, c)            
            
        while land:
            #We want to get any piece of land
            #still in the set, but we don't want
            #to remove it yet. We do that in the
            #explore function.
            piece = land.pop()
            land.add(piece)
            
            #Explore adjacent pieces of land:
            explore(piece[0], piece[1])
            islands += 1
        
        return islands