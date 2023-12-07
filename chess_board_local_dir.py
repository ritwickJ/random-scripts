# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:01:07 2022

@author: ritwick
"""
import numpy as np


class Piece:
    
    def __init__(self, orientation, x, y):
        self.o = orientation
        self.row = x
        self.column = y
        
    def go_right(self):
        if self.o == 'north':
            if self.column == 7:
                return None
            return ('west',self.row,self.column+1)
        
        if self.o == 'west':
            if self.row == 7:
                return None
            return ('south',self.row+1,self.column)
        
        if self.o == 'south':
            if self.column == 0:
                return None
            return ('east',self.row,self.column-1)
        
        if self.o == 'east':
            if self.row == 0:
                return None
            return ('north',self.row-1,self.column)
        
        
    def go_straight(self):
        if self.o == 'north':
            if self.row == 0:
                return None
            return ('north',self.row-1,self.column)
        
        if self.o == 'west':
            if self.column == 7:
                return None
            return ('west',self.row,self.column+1)
        
        if self.o == 'south':
            if self.row == 7:
                return None
            return ('south',self.row+1,self.column)
        
        if self.o == 'east':
            if self.column == 0:
                return None
            return ('east',self.row,self.column-1)


def solve(p, mv, points):

    s = p.go_straight()
    r = p.go_right()
    
    
    if s and mv[s[1],s[2]]>mv[p.row,p.column]+1:
        new_sp = Piece(s[0], s[1], s[2])
        
        mv[s[1],s[2]] = mv[p.row,p.column]+1-points[s[1],s[2]]
        
        solve(new_sp, mv, points)
        
    if r and mv[r[1],r[2]]>mv[p.row,p.column]+1:
        new_rp = Piece(r[0],r[1],r[2])

        mv[r[1],r[2]] = mv[p.row,p.column]+1-points[r[1],r[2]]
        
        solve(new_rp, mv, points)
        
    return


start = Piece('north',7,0)
m = np.reshape(np.array([1000]*64),(8,8))
m[7,0] = 0

points = np.zeros((8,8))
points[1,5] = 5
points[5,5] = 5
points[4,1] = 5
    
print(points)

solve(start,m, points)

print()

print(m)
        
        
