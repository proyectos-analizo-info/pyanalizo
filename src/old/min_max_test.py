#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_min_max(l):
    n = '\n'
    print l, n, 'min ' + str(min(l)), n, 'max ' + str(max(l)), n

if __name__ == '__main__':
    
    get_min_max([1, 2, 3, 4])
    
    get_min_max([-1, -2, -3, -4])
    
    get_min_max([-1, 2, -3, 4])
    
    get_min_max([-1, 1, 0, -2, -44])
    
    get_min_max([-0.36493102395989924, -0.3650664755151628, -0.36474058711985546, -0.36493102395989924])
