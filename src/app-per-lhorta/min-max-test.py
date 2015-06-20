#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''

def get_min_max(l):
    n = '\n'
    print l, n, 'min ' + str(min(l)), n, 'max ' + str(max(l)), n

def main():
    
    get_min_max([1, 2, 3, 4])
    
    get_min_max([-1, -2, -3, -4])
    
    get_min_max([-1, 2, -3, 4])
    
    get_min_max([-1, 1, 0, -2, -44])
    
    get_min_max([-0.36493102395989924, -0.3650664755151628, -0.36474058711985546, -0.36493102395989924])

if __name__ == '__main__':
    main()
