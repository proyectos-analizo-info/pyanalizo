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

import re

def main():
    
    def read_file(f_name):
        f_file = open(f_name, 'r')
        f_file_data = f_file.read()
        f_file.close()
        return f_file_data
    
    lines = read_file('tdata.csv').split('\n')
    
    d = {}
    
    n = '\n'
    t = '\t'
    
    f_tcsv = open('mtdata.csv', 'w')
    
    for line in lines:
        
        if line !="":
            
            line = line.split('\t') # user url date tweet
            
            print line[0]
            
            text = line[3]
            
            for match in re.finditer('http://t.co/', text):
                
                start = match.start()
                end = match.end() + 10
                
                current_value = text[start:end]
                
                new_value = "<a title='" + current_value + "' href ='" + current_value + "' target='_blank'>" + current_value + "</a>"
                
                d[current_value] = new_value
                
                
            for k in d.keys():
                
                text = text.replace(k, d[k])
            
            f_tcsv.write(line[0] + t + line[1] + t + line[2] + t + text + n)
            
        
    f_tcsv.close()

if __name__ == '__main__':
    main()
