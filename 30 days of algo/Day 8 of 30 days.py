# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:34:58 2020

@author: JADESOLA
"""

"""
There is a robot sstating at position (0,0), the origin, on a 2D plane. Given a sequence of its moves, 
judge if this robot ends up at (0,0) after it completes its moves. The move sequence is represented by
a string, the character moves[i] represents its ith move. Valid moves are R(right), L(left), U(up) and
D(down). If the robot returns to the origin after it finishes all of its moves, return true. 
Otherwise false.
"""
"""
def return_to_origin(moves):
    moves_map = {}
    for i in moves:
        moves_map[i] = moves_map.get(i,0)+1
    if ('U' and 'D' in moves) and ('R' and 'L' not in moves):
        if moves_map['U'] == moves_map['D']:
            return True
        else:
            return False
    elif ('R' and 'L' in moves) and ('U' and 'D' not in moves):
        if moves_map['L'] == moves_map['R']:
            return True
        else:
            return False
    elif 'U' and 'D' and 'L' and 'R' in moves:
        if moves_map['U'] == moves_map['D'] and moves_map['L'] == moves_map['R']:
            return True
        else:
            return False
    else:
        return False
moves = ['U','D','R','D','L','L','R','U']
print(return_to_origin(moves))
"""
def return_to_origin(moves):
    x = 0               #keeps track of movement on the x coordinate
    y = 0               #keeps track of movement on the y coordinate
    for i in moves:
        if i == 'U':
            y += 1
            print('y1',y)
        elif i == 'D':
            y -= 1
            print('y2',y)
        elif i == 'R':
            x += 1
            print('x1',y)
        elif i == 'L':
            x -= 1
            print('x2',y)
    print('y',y, 'x',x)
    if x == 0 and y == 0:
        return True
    else:
        return False
moves = ['U','D']
print(return_to_origin(moves))