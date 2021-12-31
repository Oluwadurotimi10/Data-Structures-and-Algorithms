# -*- coding: utf-8 -*-
"""
Created on Mon May 31 00:09:11 2021

@author: JADESOLA
"""

#magic square (3x3) hackerrank problem
def magic_square(s):
    possible_magic_squares=[
                            [[8,1,6],[3,5,7],[4,9,2]],
                            [[6,1,8],[7,5,3],[2,9,4]],
                            [[4,9,2],[3,5,7],[8,1,6]],
                            [[2,9,4],[7,5,3],[6,1,8]],
                            [[8,3,4],[1,5,9],[6,7,2]],
                            [[4,3,8],[9,5,1],[2,7,6]],
                            [[6,7,2],[1,5,9],[8,3,4]],
                            [[2,7,6],[9,5,1],[4,3,8]]
                            ]
    
    temp = 0 
    min_cost = float('inf')
    for magic in range(len(possible_magic_squares)):
        for i in range(len(possible_magic_squares[magic])):
            for j in range(len(possible_magic_squares[magic][i])):
                temp += abs(s[i][j]-possible_magic_squares[magic][i][j])
        min_cost = min(min_cost, temp)
        temp = 0
    return min_cost
                
            
            

s= [[4,8,2],[4,5,7],[6,1,6]]
ans = magic_square(s)
print(ans)

"""
min_cost = float('inf')
    for magic in range(len(possible_magic_squares)):
        curr_cost = 0
        for i in range(len(possible_magic_squares[magic])):
            for j in range(len(possible_magic_squares[magic][i])):
                curr_cost += abs(s[i][j]-possible_magic_squares[magic][i][j])
        if curr_cost < min_cost:
            min_cost = curr_cost     
    return min_cost
    """